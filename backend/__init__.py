from flask import Flask
from backend.views import view_blueprints

def create_server():
    app = Flask(__name__)

    for prefix, bp in view_blueprints.items():
        app.register_blueprint(bp, url_prefix=prefix)

    return app

