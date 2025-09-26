from App.database import db
from App.models import User, Student
from .user import create_user

def create_student(username, password, name, application):
    user = create_user(username, password)
    new_student = Student(user_id=user.id, name=name, password=password, application=application)
    db.session.add(new_student)
    db.session.commit()
    return new_student
