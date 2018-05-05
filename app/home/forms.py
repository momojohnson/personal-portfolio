from flask_wtf import FlaskForm, RecaptchaField
from wtforms import PasswordField, StringField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_login import login_required, login_user, logout_user
# import phonenumbers

class ContactMessageForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired("Please enter a first name")])
    last_name = StringField("Last name", validators=[DataRequired("Please enter a last name")])
    email = StringField("Email address", validators=[DataRequired("Please eneter an email address"),
                                                    Email("Email address must valid")])
    phone_number = StringField("Phone number", validators=[DataRequired("Please enter a valid phone number")])
    message = TextAreaField("Message", validators=[DataRequired("Please enter a message")])
    recaptcha = RecaptchaField()
    send_message = SubmitField("Send Message")

    # def validate_phone_number(self, field):
    #     if len(field.data) > 16:
    #         raise ValidationError("Phone number is invalid")
    #     try:
    #         input_number = phonenumbers.parse(field.data)
    #         if not phonenumbers.is_valid_number(input_number):
    #             raise ValidationError("Phone number is invalid")
    #     except:
    #         input_number = phonenumbers.parse("+1"+field.data)
    #         if not phonenumbers.is_valid_number(input_number):
    #             raise ValidationError("Phone number is invalid")
