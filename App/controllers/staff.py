from App.database import db
from App.models import User, Staff
from .user import create_user

def create_staff(username, password, name):
    user = create_user(username, password)
    new_staff = Staff(user_id=user.id, name=name, password=password)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff
