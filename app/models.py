from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login_manager

class User(UserMixin, db.Model):
    """ Create a user table """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    email = db.Column(db.String(120), unique=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password_hash = db.Column(db.String(120))
    is_admin = db.Column(db.Boolean, nullable=True, default=False)

    def __init__(self, username, email, first_name, last_name):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    @property
    def password(self):
        """ Avoid password from being accessed """
        raise AttributeError('password is not a readable attribute.')


    @password.setter
    def password(self, password):
        """ Generate password with a hash """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """ Verify hash password enter by the user """
        return check_password_hash(self.password_hash, password)

# Set up user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(70))
    phone_number = db.Column(db.String(15))
    message = db.Column(db.Text)

    def __init__(self, first_name, last_name, email, phone_number, message):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.message = message

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
