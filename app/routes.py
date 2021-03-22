from flask import render_template, flash, redirect, url_for, request
from app import app
from app.models import Book, db, Author, User
from app.form import BookForm, LoginForm, SignupForm, AuthorForm, EditBookFrom
from flask_login import  current_user, login_required, logout_user, login_user
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError




@app.route('/')
@app.route('/index')
#@login_required
def index():
    book = Book.query.all()
    return render_template('index.html', title='Home page', book=book)


@app.route('/author')
@login_required
def author_list():
    author = Author.query.all()
    return render_template('author_list.html', title='Author list page', author_list=author)


@app.route('/author/<authorid>')
def author_detail(authorid):
    author = Author.query.get(authorid)
    return render_template('author_detail.html', title='Author detail page', author=author)


@app.route('/author/add/', methods=['GET', 'POST'])
def add_author():
    form = AuthorForm()
    if form.validate_on_submit():
        add_author = Author(author_fistName=form.author_name.data)
        db.session.add(add_author)
        db.session.commit()
        flash('You add author success')
        return redirect(url_for('user_detail', user=current_user))
    return render_template('add_author.html', title="Add Author", form=form)



@app.route('/book')
@login_required
def book_list():
    book_list = Book.query.all()
    return render_template('book_list.html', title='Book list page', book=book_list)


@app.route('/book/detail/<bookid>')
def book_detail(bookid):
    book = Book.query.get(bookid)
    return render_template('book_detail.html', title='Post detail page', book=book)


@app.route('/book/add', methods=['GET', 'POST'])
@login_required
def add_book():
    form = BookForm()
    #authors = Author.query.all()
    if form.validate_on_submit():
        add_book = Book(book_name=form.book_name.data)
        db.session.add(add_book)
        db.session.commit()
        flash('You post has been created!', 'success')
        return redirect(url_for('index'))
    return render_template('add_book.html', title='add hew book', form=form)


@app.route('/book/edit<bookid>', methods=['GET', 'POST'])
def edit_book(bookid):
    form = EditBookFrom()
    book = Book.query.get(int(bookid))
    if form.validate_on_submit():
        book.book_name = form.book_name.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('book_list'))
    title = "Edit book: " + book.book_name
    return render_template('edit_book.html', title=title, form=form, book=book)


@app.route('/book/delete<bookid>')
def book_delete(bookid):
    book = Book.query.get(int(bookid))
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('book_list'))





@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    user = User.query.all()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_('Invalid username or password'))
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('auth/login.html', title='login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/signup', methods=['GET', 'POST'])
def signup_user():
    form = SignupForm()
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        print(username)
        new_user = User(username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return redirect( url_for('index'))
    return render_template('auth/signup.html', title='signup', form=form)

@app.route('/user/<user>')
def user_detail(user):
    user = User.query.get(int(current_user.user_id))
    title = "Hellow " + user.username
    return render_template('user_detail.html', title=title, user=user)

@app.route('/check')
def check():
    check = current_user
    return  render_template('check.html', title="Check page", check=check)