from flask import Blueprint, render_template

public_view_bp = Blueprint('public_v', __name__, template_folder='../templates/Public')

@public_view_bp.route('/')
def index():
    return render_template('home.html', title='Company')