from flask import Flask


def create_app(config=None):
    app = Flask(__name__, instance_relative_config=False)
    from .routes import bp

    app.register_blueprint(bp)
    return app
