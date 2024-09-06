from init import db, ma
from marshmallow import fields
from marshmallow.validate import Regexp

class User(db.Model):
    """
    This class represents the User model in the database

    Columns:
    - id: The primary key of the user
    - name: The name of the user
    - email: The email of the user
    - password: The password of the user
    - is_admin: Whether the user is an admin or not
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    """
    This property represents the relationship between a Card and its User
    The back_populates parameter is used to build the relationship between a Card and a User
    """
    cards = db.relationship("Card", back_populates="user")
    comments = db.relationship("Comment", back_populates="user")
    
class UserSchema(ma.Schema): 
    comments = fields.List(fields.Nested("CommentSchema", exclude=["user"]))
    cards = fields.List(fields.Nested("CardSchema", exclude=["user"]))

    email = fields.String(required=True, validate=Regexp("^\S+@\S+\.S+$", error="Invalid email format"))
    class Meta:
        
        fields = ("id", "name", "email", "password", "is_admin", "cards", "comments")

user_schema = UserSchema(exclude=["password"])
users_schema = UserSchema(exclude=["password"], many=True)