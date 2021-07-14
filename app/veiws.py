from app.config import app, db
#from app.db_creator import db_session
from app.forms import BookFindForm,BookAddForm
from app.model import BookModel
from flask import flash, render_template, request, redirect

from app.tables import Results


def save_changes(book, form, new=False):
    """
        Save the changes to the database
        """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    #book = BookModel()
    #book.name = form.book.data

    book.title = form.title.data
    book.author = form.author.data
    book.published = form.published.data

    if new:
        # Add the new book to the database
        db.session.add(book)
        # commit the data to the database
    db.session.commit()


@app.route('/', methods=['GET', 'POST'])
def index():
    search = BookFindForm(request.form)
    if request.method == 'POST':
         return search_results(search)
    return render_template('index.html', form=search)



@app.route('/new_book', methods=['GET', 'POST'])
def new_book():
    """
    Add a new book
    """
    form = BookAddForm(request.form)

    if request.method == 'POST' and form.validate():
        # save the album
        album = BookModel()
        save_changes(album, form, new=True)
        return redirect('/')
        flash('Album created successfully!')
    return render_template('new_book.html', form=form)


@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search.data['search'] == '':
        qry = db.session.query(BookModel)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table=table)