from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class LibroForm(FlaskForm):
    title = StringField('Title:', validators=[DataRequired()])
    author = StringField('Author:', validators=[DataRequired()])
    pages = IntegerField ('Pages:', validators=[DataRequired()])
    publish_date = DateField('Publish Date:', validators=[DataRequired()])
    description = TextAreaField('Description:', validators=[DataRequired()])
    isbn = StringField('ISBN:', validators=[DataRequired()])
    button = SubmitField('Create Book')