from App.database import db
from App.models import InternshipPosition, Employer

def create_position(title, employer_id):
    """
    Creates a new internship position.
    
    This function takes a title and an employer_id, checks if the
    employer exists, and creates a new InternshipPosition.
    """
    employer = Employer.query.get(employer_id)
    if not employer:
        print(f"Error: Employer with id {employer_id} not found.")
        return None
    
    new_position = InternshipPosition(title=title, employer_id=employer_id)
    
    try:
        db.session.add(new_position)
        db.session.commit()
        return new_position
    except Exception as e:
        db.session.rollback()
        print(f"Error creating position: {e}")
        return None

def get_all_positions():
    """
    Returns a list of all internship positions.
    """
    return InternshipPosition.query.all()

def get_all_positions_json():
    """
    Returns a list of all internship positions as JSON objects.
    """
    positions = get_all_positions()
    if not positions:
        return []
    positions_json = [position.get_json() for position in positions]
    return positions_json
