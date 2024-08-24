import os
from backend import create_server

app = create_server()

if __name__ == '__main__':
    app.run(host=os.environ.get('BACKEND_HOST', '0.0.0.0'),
            port=os.environ.get('BACKEND_PORT', 8080),
            debug=True)