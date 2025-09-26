from App.database import db
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)

    def __init__(self, username, password, role):
        self.username = username
        self.set_password(password)
        self.role = role

    def get_json(self):
        return {'id': self.id, 'username': self.username, 'role': self.role}

    def set_password(self, password):
        self.password = password

    def check_password(self, password):
        return self.password == password
