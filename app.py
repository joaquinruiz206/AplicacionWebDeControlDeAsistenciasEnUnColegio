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
    if not session.get("usuario_id"):
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

                session['usuario_id'] = usuario.id
                session["rol"] = rol
                str(rol)
                return redirect("/index"+ rol +".html")
            
            
            elif usuario == None or clave != usuario.clave:
                return render_template("iniciarSesion.html", error="Se Ingreso un Gmail o Contraseña Incorrecta.")
    
    return render_template('iniciarSesion.html')


@app.route("/indexpreceptor.html")
def iniciopreceptor():
    if session.get("rol") == "preceptor":
        usuario_id = session.get('usuario_id')
        preceptor = Preceptor.query.get(usuario_id)
        return render_template("indexpreceptor.html", usuario = preceptor)
    else:
        rol = session.get("rol")
        str(rol)
        return redirect(url_for("inicio"+ rol, error = "Ingreso no autorizado"))
    
       
    
@app.route("/indexpadre.html")
def iniciopadre():
    if session.get("rol") == "padre":
        usuario_id = session.get('usuario_id')
        padre = Padre.query.get(usuario_id)
        return render_template("indexpadre.html", usuario = padre)
    else:
        rol = session.get("rol")
        str(rol)
        return redirect(url_for("inicio"+ rol, error = "Ingreso no autorizado"))


<<<<<<< HEAD
=======
@app.route("/registraAsistencia.html")
def registraAsistencia():
    if session.get("rol") == "preceptor":
        usuario_id = session.get('usuario_id')
        preceptor = Preceptor.query.get(usuario_id)
        return render_template("registraAsistencia.html", usuario = preceptor)
    else:
        rol = session.get("rol")
        str(rol)
        return redirect(url_for("inicio"+ rol, error = "Ingreso no autorizado"))

@app.route("/informaAsistencia.html")
def informaAsistencia():
    if session.get("rol") == "preceptor":
        usuario_id = session.get('usuario_id')
        preceptor = Preceptor.query.get(usuario_id)
        return render_template("informaAsistencia.html", usuario = preceptor)
    else:
        rol = session.get("rol")
        str(rol)
        return redirect(url_for("inicio"+ rol, error = "Ingreso no autorizado"))

@app.route("/informeTotal.html")
def informeTotal():
    if session.get("rol") == "preceptor":
        usuario_id = session.get('usuario_id')
        preceptor = Preceptor.query.get(usuario_id)
        return render_template("informeTotal.html", usuario = preceptor)
    else:
        rol = session.get("rol")
        str(rol)
        return redirect(url_for("inicio"+ rol, error = "Ingreso no autorizado"))


>>>>>>> 853ee8563ce289d50dd1f9ef374ca1c17aa9af1f
@app.route("/index.html")
def pruebas():
    return render_template("index.html")


@app.route("/logout")
def logout():
    session['usuario_id'] = None
    return redirect("/")

@app.route("/asistenciahijo.html", methods = ['GET','POST'])
def asistenciahijo():
    if session.get("rol") == "padre":
        usuario_id = session.get('usuario_id')
        padre = Padre.query.get(usuario_id)
        return render_template("indexpadre.html", usuario = padre)
    
     if request.method == 'POST':
         print("Hola")
    else:
        rol = session.get("rol")
        str(rol)
        return redirect(url_for("inicio"+ rol, error = "Ingreso no autorizado"))
    
if __name__ =="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)