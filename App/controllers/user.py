from App.models import User, Student, Staff, Employer
from App.database import db
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity
from flask import g

def setup_jwt(app):
    """
    Sets up the JWTManager for authentication.
    """
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
    app.config["JWT_SECRET_KEY"] = "super-secret-key"
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def user_identity_lookup(identity):
        user = User.query.filter_by(id=identity).one_or_none()
        if user:
            return user.id
        return None

    @jwt.user_lookup_loader
    def user_lookup_callback(jwt_headers, jwt_data):
        identity = jwt_data["sub"]
        return User.query.filter_by(id=identity).one_or_none()

def add_auth_context(app):
    """
    Adds user authentication context to the request.
    This is necessary for the web application, not the CLI.
    """
    @app.before_request
    def before_request():
        g.user = None
        user_id = get_jwt_identity()
        if user_id:
            g.user = User.query.get(user_id)

def create_user(username, password, role):
    new_user = User(username=username, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    return [user.get_json() for user in users]

def create_student(username, password, first_name, last_name, email):
    new_student = Student(username=username, password=password, role="student", first_name=first_name, last_name=last_name, email=email)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def create_staff(username, password, first_name, last_name, email):
    new_staff = Staff(username=username, password=password, role="staff", first_name=first_name, last_name=last_name, email=email)
    db.session.add(new_staff)
    db.session.commit()
    return new_staff

def create_employer(username, password, company_name, company_info, email):
    new_employer = Employer(username=username, password=password, role="employer", company_name=company_name, company_info=company_info, email=email)
    db.session.add(new_employer)
    db.session.commit()
    return new_employer