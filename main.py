from flask import Flask ,render_template  # importamos la libreria
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# nota las configuraciond se guaran entre cochetes no parentesos por que es un array
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:////home/richard/proyectos_Pyhton/Blocg_flask/blog.db"
## se configuro la ruta de la base de datos 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Nota: normalemnte estes codigo va dentro de otro archivo
class Post(db.Model): # creando la tabal de la bse de datos 
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String, nullable = False)
    fecha = db.Column(db.DateTime, default = datetime.now)
    texto = db.Column(db.String, nullable = False)
# Nota : luego de crear la estructura de la tabla abrimos una terminal y creamos al DB
# escribimos en treminal pyhton3       .. dentro de pyhton escribimos
# from main import db
# db.create_all()            con esto abremos creado el archoivo de la bd
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# rutas de paginas 
@app.route("/")
def inicio():
    posts = Post.query.orden_by(Post.fecha.desc()).all()
    return render_template("inicio.html" , posts = posts)

@app.route("/agregar")
def agregar():
    return render_template(agregar.html)

if __name__ == "__main__":
    app.run(debug=True)


