from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "newsdatabase.db"))

# Config app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['JSON_AS_ASCII'] = False

app.secret_key = "flask rocks!"
db = SQLAlchemy(app)