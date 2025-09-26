import click
from flask.cli import with_appcontext
from App.database import create_db, get_migrate
from App.main import create_app
from App.controllers import (
    create_user, get_all_users, get_all_users_json,
    create_student, create_staff, create_employer
)

app = create_app()
migrate = get_migrate(app)

@app.cli.command("init", with_appcontext=True)
def initialize():
    create_db(app)
    print("Database initialized successfully!")

@click.group("user")
def user_commands():
    pass

@user_commands.command("create")
@click.argument("username")
@click.argument("password")
@click.argument("role")
def create_user_command(username, password, role):
    create_user(username, password, role)
    print(f"User {username} with role {role} created!")

@user_commands.command("list")
def list_users_command():
    users = get_all_users_json()
    print(users)

@user_commands.command("create-student")
@click.argument("username")
@click.argument("password")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("email")
def create_student_command(username, password, first_name, last_name, email):
    create_student(username, password, first_name, last_name, email)
    print(f"Student {first_name} {last_name} created!")

@user_commands.command("create-staff")
@click.argument("username")
@click.argument("password")
@click.argument("first_name")
@click.argument("last_name")
@click.argument("email")
def create_staff_command(username, password, first_name, last_name, email):
    create_staff(username, password, first_name, last_name, email)
    print(f"Staff {first_name} {last_name} created!")

@user_commands.command("create-employer")
@click.argument("username")
@click.argument("password")
@click.argument("company_name")
@click.argument("company_info")
@click.argument("email")
def create_employer_command(username, password, company_name, company_info, email):
    create_employer(username, password, company_name, company_info, email)
    print(f"Employer {company_name} created!")

app.cli.add_command(user_commands)