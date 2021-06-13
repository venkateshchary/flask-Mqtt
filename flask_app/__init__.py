from flask import Flask
from flask_cors import CORS


def create_app():
    try:
        app = Flask(__name__, instance_relative_config=True)
        CORS(app)
        from .common.mqtt_client import init_mqtt
        init_mqtt()

        @app.route("/")
        def home():
            return "<h1>Welcome to flask mqtt integration service<h1>"
        return app
    except Exception as e:
        raise e
