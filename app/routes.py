from flask import render_template
from app import app
from app.models import Book


@app.route('/')
@app.route('/index')
def index():
    book = Book.query.all()
    return render_template('index.html', title='Home page', book=book)


