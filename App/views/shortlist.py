from flask import Blueprint, jsonify
from App.models import Shortlist, InternshipPosition

shortlist_views = Blueprint('shortlist_views', __name__)

@shortlist_views.route('/student/<int:student_id>/shortlist')
def view_student_shortlist(student_id):
    shortlist_items = Shortlist.query.filter_by(student_id=student_id).all()
    return jsonify([item.get_json() for item in shortlist_items])

@shortlist_views.route('/employer/<int:employer_id>/shortlist')
def view_employer_shortlist(employer_id):
    positions = InternshipPosition.query.filter_by(employer_id=employer_id).all()
    position_ids = [p.id for p in positions]
    shortlist_items = Shortlist.query.filter(Shortlist.position_id.in_(position_ids)).all()
    return jsonify([item.get_json() for item in shortlist_items])