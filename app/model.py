from app.config import db

class BookModel(db.Model):
    __tablename__ = "mybook"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    published = db.Column(db.String)

    def __repr__(self):
        return 'BookModel(title =%s,author=%s,published=%s)' %(self.title, self.author, self.published)
