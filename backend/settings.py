import os

BACKEND_HOST = os.environ.get('BACKEND_HOST', '0.0.0.0')
BACKEND_PORT = os.environ.get('BACKEND_PORT', 8080)
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://admin:password@localhost:5432/company')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)