from App.database import db
from App.models import User, Employer
from .user import create_user

def create_employer(username, password, name):
    user = create_user(username, password)
    new_employer = Employer(user_id=user.id, name=name, password=password)
    db.session.add(new_employer)
    db.session.commit()
    return new_employer
