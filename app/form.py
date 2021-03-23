from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, ValidationError, EqualTo



class BookForm(FlaskForm):
    book_name = StringField('Book name', validators=[DataRequired()])
    authors = SelectField('Seleck author', choices=[])
    submit = SubmitField('Submit')


class EditBookFrom(FlaskForm):
    book_name = StringField('New name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class AuthorForm(FlaskForm):
    author_name = StringField('Book name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class EditAuthorFrom(FlaskForm):
    author_fistName = StringField('New name', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    first_name = StringField('first name', validators=[DataRequired()])
    last_name = StringField('last name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sing in')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sing in')