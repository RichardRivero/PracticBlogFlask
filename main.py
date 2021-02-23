from flask import Flask ,render_template,request, redirect  # importamos la libreria
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# nota las configuracion SQL se guardan entre cochetes no parentesos por que es un array
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/richard/proyectos_Pyhton/Blocg_flask/blog.db"
## se configuro la ruta de la base de datos 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Nota: normalemnte estes codigo va dentro de otro archivo
class Post(db.Model): # creando la tabal de la bse de datos 
    __tablename__ = "posts"     
    id      = db.Column(db.Integer, primary_key = True)
    titulo  = db.Column(db.String, nullable = False)
    fecha   = db.Column(db.DateTime, default = datetime.now)
    texto   = db.Column(db.String, nullable = False)
# Nota : luego de crear la estructura de la tabla abrimos una terminal y creamos al DB
# escribimos en treminal pyhton3       .. dentro de pyhton escribimos
# from main import db
# db.create_all()            con esto abremos creado el archoivo de la bd
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# rutas de paginas 
@app.route("/")
def inicio():
    posts = Post.query.order_by(Post.fecha.desc()).all()
    return render_template("inicio.html" , posts = posts)

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")

@app.route("/crear", methods=["POST"])
def crear_post():
    titulo = request.form.get("titulo") # la concexion se hace con el nombre de la etiqueta que se colo en la apgina agregar
    texto = request.form.get("texto")
    post = Post(titulo=titulo, texto=texto)
    db.session.add(post)
    db.session.commit() 
    return redirect("/")  # el metodo redirecciona a otra direccion

@app.route("/otros")
def otros():
    return render_template("otros.html")

if __name__ == "__main__":
    app.run(debug=True)


