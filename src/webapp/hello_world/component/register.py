from src.webapp.hello_world.component.greeter.greeter import greeter
from src.webapp.hello_world.component.message_board.message_board import message_board
from flask import Flask


def register_components(app: Flask) -> None:
    app.register_blueprint(greeter)
    app.register_blueprint(message_board, url_prefix='/messages')
