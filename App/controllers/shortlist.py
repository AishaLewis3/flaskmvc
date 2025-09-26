from App.database import db
from App.models import Shortlist

def add_shortlist_item(student_id, staff_id, position_id):
    new_shortlist = Shortlist(student_id=student_id, staff_id=staff_id, position_id=position_id)
    db.session.add(new_shortlist)
    db.session.commit()
    return new_shortlist

def get_all_shortlists():
    return Shortlist.query.all()

def get_all_shortlists_json():
    shortlists = get_all_shortlists()
    if shortlists:
        return [shortlist.to_dict() for shortlist in shortlists]
    return []
