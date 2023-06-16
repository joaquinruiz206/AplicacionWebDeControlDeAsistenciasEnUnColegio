from datetime import datetime
from flask  import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Estudiante,Preceptor,Padre,Curso,Asistencia

@app.route('/')

def inicio():
    return render_template('index.html')

@app.route('/iniciarSesion', method = ["GET","POST"])

def iniciarSesion():
    if request.method == "POST":
        if not request.form["usuario"] or request.form["contraseña"] or request.form["rol"]:
            return render_template('error.html', error=("Los datos ingresados no son los correctos."))
        else:
            datos_form = request.form
            usuario = request.form["usuario"]
            contraseña = request.form["constraseña"]
            rol = request.form["rol"]
            if request.form["rol"]:
            db.session.
    return render_template('iniciarSesion.html')
    
