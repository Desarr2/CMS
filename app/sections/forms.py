from flask.ext.wtf import Form # , RecaptchaField
from wtforms import TextField, PasswordField, SubmitField  # BooleanField
from wtforms import TextAreaField, HiddenField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import Required, Email, EqualTo, Length, Regexp
from wtforms import StringField, BooleanField, PasswordField, TextField , TextAreaField # BooleanField

strip_filter = lambda x: x.strip() if x else None

class CreateSectionForm(Form):
	section = StringField('section', filters=[strip_filter])
	description = TextAreaField('description', filters=[strip_filter])


class EditSectionForm(Form):
	section = StringField('section', filters=[strip_filter])
	description = TextAreaField('description', filters=[strip_filter])