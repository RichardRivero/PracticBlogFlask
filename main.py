from flask import Flask# importamos la libreria
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config("SQLALCHEMY_DATABASE_URI") = "sqlite:/home/richard/proyectos Pyhton/Blocg_flask/blog.db
"
## se configuro la ruta de la base de datos 
app.config("SQLALCHEMY_TRACK_MODIFICATIONS") = False

db = SQLAlchemy(app)


class Post(db.Model):
    


