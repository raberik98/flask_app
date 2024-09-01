from flask import Flask
from flask_migrate import Migrate

from .extensions import db
from .settings import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS  

def create_app():
    # Flask app setup
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

    # View blueprints are imported
    from backend.views.public import public_view_bp
    # View blueprints are registered
    app.register_blueprint(public_view_bp)

    # Controller blueprints are imported
    from backend.controllers.employee import employee_controller_bp
    # Controller blueprints are registered 
    app.register_blueprint(employee_controller_bp)

    # Database setup
    db.init_app(app)
    migrate = Migrate(app, db)

    return app