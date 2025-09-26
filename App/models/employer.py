from App.database import db
from .user import User

class Employer(User):
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    company_name = db.Column(db.String(120), nullable=False)
    company_info = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Relationships to other models
    positions = db.relationship('InternshipPosition', backref='employer', lazy=True)

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'company_name': self.company_name,
            'company_info': self.company_info,
            'email': self.email
        }