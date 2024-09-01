from flask import Blueprint, request
from backend.models.employee_model import Employee

employee_controller_bp = Blueprint('employee_c', __name__, url_prefix='/api')


@employee_controller_bp.route('/employees', methods=['GET'])
def getAllEmployees():
    employees = Employee.query.all()

    return str(employees)


    