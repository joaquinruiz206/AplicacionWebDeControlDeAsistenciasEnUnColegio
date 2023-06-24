from datetime import datetime
from flask  import Flask, request, render_template, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
app.config.from_pyfile('config.py')



from models import db
from models import Estudiante,Preceptor,Padre,Curso,Asistencia

@app.route('/')
def inicio():
    if not session.get("correo"):
        return redirect('iniciarSesion.html')

@app.route('/usuarios')
def obtenerUsuarios():
    usuarios = Preceptor.query.all()  # Obtener todos los usuarios (Preceptores)
    return render_template('usuarios.html', usuarios=usuarios)

@app.route('/iniciarSesion.html', methods = ['GET', 'POST'])
def iniciarSesion():
    if request.method == "POST":
        if not request.form["usuario"] or not request.form["contraseña"] or not request.form["rol"]:
            return render_template("iniciarSesion.html", error="Ingrese correo y contraseña")
        else:
            clave = request.form["contraseña"]
            rol = request.form["rol"]
            correo = request.form["usuario"]

                
            if rol == "preceptor":
                usuario = Preceptor.query.filter_by(correo=correo).first()
            elif rol == "padre":
                usuario = Padre.query.filter_by(correo=correo).first()
            
            
            

            if usuario and usuario.clave == clave:

                session["correo"] = request.form.get("correo")
                session["rol"] = rol
                str(rol)
                return redirect("/index"+ rol +".html")
            
            
            elif usuario == None or clave != usuario.clave:
                return render_template("iniciarSesion.html", error="Se Ingreso un Gmail o Contraseña Incorrecta.")
    
    return render_template('iniciarSesion.html')


@app.route("/indexpreceptor.html")
def inicioPreceptor():
    if session.get("rol") == "preceptor":
        return render_template("indexpreceptor.html")
    else:
        return redirect(url_for('inicioPadre', error = "Ingreso no autorizado"))
       
    
@app.route("/indexpadre.html")
def inicioPadre():
    if session.get("rol") == "padre":
        return render_template("indexpadre.html")
    else:
        return redirect(url_for('inicioPreceptor', error = "Ingreso no autorizado"))



@app.route("/index.html")
def pruebas():
    return render_template("index.html")


@app.route("/logout")
def logout():
    session["correo"] = None
    return redirect("/")

if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)