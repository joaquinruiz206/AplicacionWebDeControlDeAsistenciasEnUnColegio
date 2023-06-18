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

@app.route('/iniciarSesion.html', methods = ['GET', 'POST'])
def iniciarSesion():
    if request.method == "POST":
        if not request.form["usuario"] or not request.form["contraseña"] or not request.form["rol"]:
            return render_template('error.html', error=("Los datos ingresados no son los correctos."))
       
        else:
            contraseña = request.form["contraseña"]
            rol = request.form["rol"]
            usuario = request.form["usuario"]
            datos_form = request.form
            print(datos_form)
            if request.form["rol"] =="":
                print("HOLA")

    return render_template('iniciarSesion.html')

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)