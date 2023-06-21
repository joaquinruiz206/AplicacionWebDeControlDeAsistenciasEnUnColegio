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

@app.route('/usuarios')
def obtenerUsuarios():
    usuarios = Preceptor.query.all()  # Obtener todos los usuarios (Preceptores)
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/iniciarSesion.html', methods = ['GET', 'POST'])
def iniciarSesion():
    if request.method == "POST":
        if not request.form["usuario"] or not request.form["contraseña"] or not request.form["rol"]:
            return render_template('error.html', error=("Los datos ingresados no son los correctos."))
        else:
            clave = request.form["contraseña"]
            rol = request.form["rol"]
            correo = request.form["usuario"]
            
            if rol == "preceptor":
                usuario = Preceptor.query.filter_by(correo=correo).first()
            elif rol == "padre":
                usuario = Padre.query.filter_by(correo=correo).first()
            if usuario and usuario.clave == clave:
                return render_template("index.html")
            elif usuario == None or clave != usuario.clave:
                return render_template("error.html", error = ("Datos ingresados incorrectos"))
    return render_template('iniciarSesion.html')

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)