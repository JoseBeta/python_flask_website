from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from web_flask.config import Config


db = SQLAlchemy()
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)

    from web_flask.main.routes import main
    app.register_blueprint(main)

    return app