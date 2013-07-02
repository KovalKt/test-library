from flask import render_template, url_for, redirect, request, abort
from . import app, db
from .models import Author, Book
from .forms import NewBook, NewAuthor

PER_PAGE = 5


@app.route('/')
@app.route('/authors', methods=("GET", "POST"))
def author_list():
    if request.method == "POST":
        search_query = "%{}%".format(request.form['search_query'])
        authors = Author.query.filter(Author.first_name.like(search_query)).all()
        authors.extend(Author.query.filter(Author.last_name.like(search_query)).all())
        authors = list(set(authors))
    else:
        authors = Author.query.all()
    return render_template("author_list.html", authors=authors)


@app.route('/books/', defaults={'page': 1})
@app.route('/books/page/<int:page>')
def book_list(page):

    pagination = Book.query.paginate(page, per_page=PER_PAGE)
    return render_template("book_list.html", pagination=pagination)


@app.route('/add-author', methods=("GET", "POST"))
def add_author():
    form = NewAuthor(request.form)
    if request.method == "POST":
        if form.validate():
            new_author = Author(form.fname.data, form.lname.data)
            db.session.add(new_author)
            db.session.commit()
            if form.add_book:
                return redirect(url_for('add_book', id=new_author.id))
            return redirect(url_for('author_list'))
    return render_template('new_author.html', form=form)


@app.route('/add-book-for/<author_id>', methods=("GET", "POST"))
def add_book(author_id):
    form = NewBook(request.form)
    if request.method == "POST":
        if form.validate():
            new_book = Book(form.name.data, form.year.data)
            author = Author.query.get(author_id)
            author.books.append(new_book)
            db.session.add(new_book)
            db.session.commit()
            return redirect(url_for('author_list'))
    return render_template('new_book.html', form=form, author_id=author_id)


@app.route('/author-info/<id>')
def author_info(id):
    author = Author.query.get(id)
    if author is None:
        abort(404)
    return render_template('author_info.html', author=author)


@app.route('/book-info/<id>')
def book_info(id):
    book = Book.query.get(id)
    if book is None:
        abort(404)
    return render_template('book_info.html', book=book)
