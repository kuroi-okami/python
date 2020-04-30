from src.webapp.hello_world.component.greeter.greeter import greeter
from flask import Flask


def register_components(app: Flask) -> None:
    app.register_blueprint(greeter)
