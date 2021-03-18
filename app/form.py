from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class BookForm(FlaskForm):
    book_name = StringField('Book name', validators=[DataRequired()])
    # author_name = StringField('SAuthor name', validators=[DataRequired()])
    submit = SubmitField('Submit')