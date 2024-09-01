from backend import create_app
from backend.settings import BACKEND_HOST, BACKEND_PORT

if __name__ == '__main__':
    app = create_app()

    app.run(host=BACKEND_HOST,

            port=BACKEND_PORT,
            debug=True)

    
