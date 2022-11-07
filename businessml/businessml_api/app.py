from flask import Flask
from waitress import serve
from .api import app_routes


def create_app(testing=False):
    """Application factory, used to create application"""
    app = Flask(__name__)

    app.config.from_object("businessml_api.config")
    if testing is True:
        app.config["TESTING"] = True

    register_blueprints(app)
    return app


def register_blueprints(app):
    """Register all blueprints for application"""
    app.register_blueprint(app_routes.http)


if __name__ == "__main__":
    app = create_app()
    serve(app, port=8000, url_scheme="https")
    