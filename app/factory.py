from flask import Flask


def create_app():
    application = Flask(__name__)
    from app.main import main
    application.register_blueprint(main)
    return application
