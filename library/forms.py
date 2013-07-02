from flask.ext.wtf import Form
from flask.ext.wtf.html5 import IntegerField
from wtforms import TextField, validators, BooleanField


class NewBook(Form):
    name = TextField('Name', [validators.Required(), validators.Length(min=3, max=64, message='Wrong name')])
    year = IntegerField('Year', [validators.NumberRange(min=600, max=2013, message='Wrong year')])


class NewAuthor(Form):
    first_name = TextField('Firts name', [validators.Required(), validators.Length(min=2, message='Too short first name')])
    last_name = TextField('Last name', [validators.Length(min=2, message='Too short last name')])
    add_book = BooleanField('Add book')
