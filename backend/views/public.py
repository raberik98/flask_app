from flask import Blueprint, render_template, request
from backend.models.employee_model import Employee

public_view_bp = Blueprint('public_v', __name__, template_folder='../templates/Public')

@public_view_bp.route('/')
def index():
    uid = 12
    permission = Employee.get_permission(uid)
    return render_template('home.html',
                            title='Company',
                            user_permission=permission,
                            breadcrumbs=[
                                {"text": "Home", "href": "#"},
                                {"text": "Library", "href": "#"},
                                {"text": "Data", "href": "#"}
                            ]
                        )