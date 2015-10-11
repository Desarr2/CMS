from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, TextField
from wtforms.validators import Required, DataRequired, Email, EqualTo

class RecoverPassForm(Form):
	email = TextField('Email Address', [Email(), Required(message='Forgot your email address?')])

class ResetPasswordSubmit(Form):
	password = PasswordField('Password', validators = [DataRequired()])
	confirm = PasswordField('Confirm Password')

	class CreateUserForm(Form):
		id = StringField('id', validators=[DataRequired()])
		nickname = StringField('nickname', validators=[DataRequired()])
		email = StringField('email', validators=[DataRequired()])
		password = PasswordField('pass', validators=[DataRequired()])