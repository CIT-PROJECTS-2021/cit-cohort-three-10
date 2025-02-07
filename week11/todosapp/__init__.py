import os
from sqlalchemy import MetaData
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_mail import Mail
from flask_migrate import Migrate



convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
}

metadata = MetaData(naming_convention=convention)

db = SQLAlchemy(metadata=metadata)
ma = Marshmallow()
migrate = Migrate()
api = Api()
jwt = JWTManager()
mail = Mail()
cors = CORS()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "weowiueroieufm"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todos.db"
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    from .erros.handlers import errors
    app.register_blueprint(errors)


    return app



from .auth import auth_routes


auth_routes(api)