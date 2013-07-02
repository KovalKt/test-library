from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

association = db.Table('association', db.Column('author', db.Integer, db.ForeignKey('author.id')), db.Column('book', db.Integer, db.ForeignKey('book.id')))


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(32), nullable=False)
    last_name = db.Column(db.String(64))
    books = db.relationship('Book', secondary=association, backref='authors', lazy='dynamic')

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        print "Author id:{}".format(self.id)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    year = db.Column(db.Integer)

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def __repr__(self):
        print "Book id:{}".format(self.id)
