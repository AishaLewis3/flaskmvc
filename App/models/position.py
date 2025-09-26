from App.database import db

class InternshipPosition(db.Model):
    __tablename__ = 'internship_position'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'), nullable=False)
    
    def get_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'employer_id': self.employer_id
        }
