from app import db, login
from sqlalchemy.orm import relationship
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


book_author = db.Table('student_identifier',
    db.Column('book_id', db.Integer, db.ForeignKey('book.book_id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.author_id'))
)


class Author(db.Model):
    __tablename__ = 'author'
    author_id = db.Column(db.Integer, primary_key=True)
    author_fistName = db.Column(db.String(64))


class Book(db.Model):
    __tablename__ = 'book'
    book_id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(128), unique=True)
    authors = db.relationship("Author", secondary=book_author)


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(128), index=True)
    last_name = db.Column(db.String(128), index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '{}'.format(self.user_id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
           return (self.user_id)


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))