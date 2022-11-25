from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .routes.rick_y_morty import rick_y_morty

def create_app():
    app= Flask(__name__)
    app.config.from_object(Config)

    Bootstrap(app)

    app.register_blueprint(blueprint=rick_y_morty)
    # SQLAlchemy(app)
    # Moment(app)
    return app