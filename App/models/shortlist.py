from App.database import db

class Shortlist(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    position_id = db.Column(db.Integer, db.ForeignKey('internship_position.id'))
    staff_id = db.Column(db.Integer, db.ForeignKey('staff.id'))
    status = db.Column(db.String(20), default='shortlisted')

    def __init__(self, student_id, staff_id):
        self.student_id = student_id
        self.staff_id = staff_id

    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'position_id': self.position_id,
            'staff_id': self.staff_id,
            'status': self.status
        }
