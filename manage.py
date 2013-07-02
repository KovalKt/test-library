from flask.ext.script import Manager
from library import app

manager = Manager(app)


@manager.command
def init_db():
    '''Initialise database. Create schema'''
    from . import app, db
    with app.app_context():
        db.create_all()


@manager.command
def add_records_for_test():
    '''Add few test records to table Author and Book '''
    from . import app, db
    from models import Author, Book
    with app.app_context():
        author1 = Author('Ivan', 'Ivanov')
        book1 = Book('PROLOG', 1993)
        author1.books.append(book1)
        book2 = Book('ADA95', 1995)
        author1.books.append(book2)
        author2 = Author('Vasil', 'Petrov')
        author2.books.append(book1)
        book3 = Book('Pascal', 1998)
        author3 = Author('Serey', 'Guk')
        author3.books.append(book3)
        db.session.add(author1)
        db.session.add(book1)
        db.session.add(author2)
        db.session.add(book2)
        db.session.add(author3)
        db.session.add(book3)
        db.session.commit()

if __name__ == "__main__":
    manager.run()
