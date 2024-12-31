from flask import Flask

from .events import socketio
from .config import AppConfig
from .routes import bp


def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_object(AppConfig)

    app.register_blueprint(bp)

    socketio.init_app(app)

    return app