from app import db
from sqlalchemy.orm import relationship


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
