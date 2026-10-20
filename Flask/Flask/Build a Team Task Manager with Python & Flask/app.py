from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from models import User, Task

app = Flask(__name__)
app.config['SECRET_KEY'] = 'teamtasksecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Loading user data
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        role = request.form.get('role', 'member')

        if User.query.filter_by(username = username).first():
            flash('Username already exists!', 'danger')
            return redirect(url_for('register'))
        
        new_user = User(username = username, password = password, role = role )
        db.session.add(new_user)
        db.session.commit()
        flash('Registered successfully!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username = username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('admin_dashboard' if user.role == 'admin' else 'dashboard'))
    flash('Invalid credentials', 'danger')
    return render_template('login.html')
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    my_tasks = Task.query.filter_by(created_by = current_user.id).all()
    shared_tasks = Task.query.filter_by(shared_with = current_user.id).all()
    return render_template('dashboard.html', my_tasks = my_tasks, shared_tasks = shared_tasks)


@app.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash("Access denied", 'danger')
        return redirect(url_for('dashboard'))
    
    tasks = Task.query.all()
    return render_template('admin_dashboard.html', tasks = tasks)

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        shared_with_id = int(request.form['shared_with'])
        new_task =  Task(title = title, description = description, created_by = current_user.id, shared_with = shared_with_id)

        db.session.add(new_task)
        db.session.commit()

        flash('Task added!', 'success')

    users = User.query.filter(User.id != current_user.id).all()
    return render_template('add_task.html', users = users)


@app.route('/edit/<int:task_id>', methods = ['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if  current_user.id != task.created_by and current_user.role != 'admin':
        flash("Access denied", "danger")
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.status = request.form['status']

        db.session.commit()
        flash('Task  updated', 'success')
        return redirect(url_for('dashboard'))
    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if current_user.id != task.created_by and current_user.role != 'admin':
        flash("Access denied", "danger")
        return redirect(url_for('dashboard'))
    
    db.session.delete(task)
    db.session.commit()

    flash('Task deleted', 'success')
    return redirect(url_for('dashboard'))

# Executing the App

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)