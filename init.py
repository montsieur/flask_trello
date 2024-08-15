from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Mashmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy
ma = Mashmallow
bcrypt = Bcrypt
jwt = JWTManager

