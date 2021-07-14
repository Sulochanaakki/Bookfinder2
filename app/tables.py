from flask_table import Table, Col
class Results(Table):
    id = Col('Id', show=False)
    title = Col('Title')
    author = Col('author')
    published = Col('Published')
