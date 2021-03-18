from flask import render_template, flash, redirect, url_for, request
from app import app
from app.models import Book, db, Author
from app.form import BookForm




@app.route('/')
@app.route('/index')
def index():
    book = Book.query.all()
    return render_template('index.html', title='Home page', book=book)


@app.route('/author')
def author_list():
    author = Author.query.all()
    return render_template('author_list.html', title='Author list page', author_list=author)


@app.route('/author/<authorid>')
def author_detail(authorid):
    author = Author.query.get(authorid)
    return render_template('author_detail.html', title='Author detail page', author=author)


@app.route('/book')
def book_list():
    book_list = Book.query.all()
    return render_template('book_list.html', title='Book list page', book_list=book_list)


@app.route('/book/detail/<bookid>')
def book_detail(bookid):
    book = Book.query.get(bookid)
    return render_template('book_detail.html', title='Post detail page', book=book)


@app.route('/book/add', methods=['GET', 'POST'])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        add_book = Book(book_name=form.book_name.data)
        db.session.add(add_book)
        db.session.commit()
        flash('You post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('add_book.html', title='add hew book', form=form)

@app.route('/login')
def login():
    return render_template('login.html', title='login')

