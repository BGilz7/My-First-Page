from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

class EmailForm(FlaskForm):
    email = StringField('Email:', validators=[DataRequired(), Email()])
    message = StringField('Message:', validators=[DataRequired()])
    submit = SubmitField('Submit')
