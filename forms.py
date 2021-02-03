from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Email

class SignUpForm(FlaskForm):
    email = EmailField('E-mail', validators=[Email()])
    prijava = SubmitField('Prijava')