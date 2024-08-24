from flask import Blueprint, render_template

public_view_bp = Blueprint('public_v', __name__)

@public_view_bp.route('/')
def index():
    return '<h1>Public</h1>'