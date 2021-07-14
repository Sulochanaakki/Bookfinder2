
from app.config import db

from app.veiws import *
#init_db()
db.create_all()

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True)