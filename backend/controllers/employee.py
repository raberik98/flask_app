from flask import Blueprint, request, jsonify
from backend.models.employee_model import Employee

employee_controller_bp = Blueprint('employee_c', __name__, url_prefix='/api')


@employee_controller_bp.route('/employees', methods=['GET'])
def getAllEmployees():
    employees = Employee.query.all()
    employees_list = [employee.to_dict() for employee in employees]

    return jsonify(employees_list)


@employee_controller_bp.route('/employee/<int:id>', methods=['GET'])
def employeeById(id):
    selected_employee = Employee.query.get(id)

    return jsonify(selected_employee)
    