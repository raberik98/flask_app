from .public import public_view_bp
from .auth import auth_view_bp
from .admin import admin_view_bp

view_blueprints = {
    '/': public_view_bp,
    '/auth': auth_view_bp,
    '/admin': admin_view_bp
}