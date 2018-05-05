from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_login import login_required, login_user, logout_user

class RegisterUserForm(FlaskForm):
    """
    A form that is used to register a user
    """
    username = StringField('Username', validators=[DataRequired('Please enter a valid username')])
    email = StringField('Email', validators=[DataRequired("Please enter an email"),
    Email("Please enter a valid email address")])
    first_name = StringField("First name", validators[DataRequired("Please enter a first name")])
    last_name = StringField("Last name", validators=[DataRequired("Please enter a last name")])
    password = PasswordField("Password",validators=[DataRequired("Please enter password"), EqualTo('confirmed_password')])
    confirmed_password = PasswordField("Confirmed password", validators=[DataRequired("Please confirmed password"), Message="password must matched"])
    submit = SubmitField("Register")

    def validate_email(self, field):
		"""
		Avoid duplicate email registration by raising validation error if email exist

		"""
		if User.query.filter_by(email=field.data).first():
			raise ValidationError("This email has been registered")

	def validate_username(self, field):
		"""
		Avoid duplicate username registration by raising validation error if username exist
		"""
		if User.query.filter_by(username=field.data).first():
			raise ValidationError("This username has already been registered")
