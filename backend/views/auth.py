from flask import Blueprint, render_template

auth_view_bp = Blueprint('auth_v', __name__)

@auth_view_bp.route('/')
def index():
    return '<h1>Auth</h1>'