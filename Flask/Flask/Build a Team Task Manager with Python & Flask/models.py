from extensions import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    role = db.Column(db.String(10), default = 'member') # Admin and Member
    created_tasks = db.relationship('Task', backref='creator', foreign_keys='Task.created_by', lazy=True)
    shared_task = db.relationship('Task', backref='receiver', foreign_keys='Task.shared_with', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='Pending')
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    shared_with = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)