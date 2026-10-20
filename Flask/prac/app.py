from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Secret key for session to work securely
app.secret_key = 'your_secret_key'

# Route to display home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle sign-up form submission
@app.route('/sign_up', methods=['POST'])
def sign_up():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    # For simplicity, assume the sign-up is successful and store user info in session
    session['logged_in'] = True  # Set user as logged in
    session['name'] = name
    session['email'] = email
    
    return redirect(url_for('profile'))

# Route to handle sign-in form submission
@app.route('/sign_in', methods=['POST'])
def sign_in():
    email = request.form['email']
    password = request.form['password']

    # For simplicity, assume the sign-in is successful and store user info in session
    session['logged_in'] = True  # Set user as logged in
    session['email'] = email

    return redirect(url_for('profile'))

# Route to display profile page
@app.route('/profile')
def profile():
    # Check if the user is logged in, if not, redirect to home page
    if 'logged_in' not in session or not session['logged_in']:
        return redirect(url_for('home'))  # Redirect to home if not logged in
    
    name = session.get('name', 'Guest')  # Default to 'Guest' if no name in session
    email = session.get('email', 'N/A')  # Default to 'N/A' if no email in session

    return render_template('profile.html', name=name, email=email)

# Route to handle log-out
@app.route('/logout')
def logout():
    # Remove user info from the session and redirect to home page
    session.pop('logged_in', None)
    session.pop('name', None)
    session.pop('email', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
