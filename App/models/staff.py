from App.database import db
from .user import User

class Staff(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relationships to other models
    shortlist_items = db.relationship('Shortlist', backref='staff', lazy=True)

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
