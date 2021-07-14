from wtforms import Form, StringField, SelectField
class BookFindForm(Form):
    choices = [('title', 'title'),
               ('author', 'author'),
               ('published', 'published')]
    select = SelectField('Search for book:', choices=choices)
    search = StringField('')


class BookAddForm(Form):
    title = StringField('Title')
    author = StringField('Author')
    published = StringField('Published')