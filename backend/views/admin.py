from flask import Blueprint, render_template

admin_view_bp = Blueprint('admin_v', __name__)

@admin_view_bp.route('/')
def index():
    return '<h1>ADMIN</h1>'