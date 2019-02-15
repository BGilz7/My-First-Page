from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    email = StringField('Enter message here ', validators=[DataRequired()])
    message = StringField('Enter message here ', validators=[DataRequired()])
    submit = SubmitField('Submit')
