from flask import Flask
from src.webapp.hello_world.component.register import register_components


if __name__ == '__main__':
    app = Flask(__name__)
    register_components(app)
    app.run(host='0.0.0.0', port=5000)
