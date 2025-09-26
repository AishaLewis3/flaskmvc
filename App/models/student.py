from App.database import db
from datetime import datetime
from App.models.user import User   # ✅ import User properly

class Student(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    registration_date = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships to other models
    shortlist_items = db.relationship('Shortlist', backref='student', lazy=True)

    def __init__(self, username, password, first_name, last_name, email, role="student"):
        super().__init__(username=username, password=password, role=role)
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'registration_date': self.registration_date.isoformat()
        }
