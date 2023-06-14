from __main__ import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class Curso(db.model):
    __tablename__="Curso"
    id= db.Column(db.Integer, primary_key=True)
    ano=db.Column(db.Integer, nullable=False)
    division=db.Column(db.Integer, bullable=False)
    

class Preceptor(db.model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(40),nullable=False)
    apellido=db.Column(db.String(40),nulleable=False)
    correo=db.Column(db.String(40),unique=True, nullable=False)
    clave=db.Column(db.String(80),nullable=False)
    cursos=db.relationship('curso',backref='preceptor')
    


class Estudiante(db.Model): 
    __tablename__ = "estudiante"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(40), nullable = False)
    apellido = db.Column(db.String(40), nullable = False)
    dni = db.Column(db.String(20), nullable = False)
    idcurso = db.Column(db.Integer, nullable = False)
    idpadre = db.Column(db.Integer, nullable = False)

        

class Asistencia:
    __tablename__ = "asistencia"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, nullable = False)
    codigoClase = db.Column(db.Integer, nullable = False)
    asistio = db.Column(db.String(1), nullable = False)
    justificacion = db.Column(db.Text, nullable = False)
    idestudiante = db.Column(db.Integer, nullable = False)
    


class Padre:
    __tablename__ = "padre"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(40), nullable = False)
    apellido = db.Column(db.String(40), nullable = False)
    correo = db.Column(db.String(50), unique = True, nullable = False)
    clave = db.Column(db.String(50),unique = True, nullable = False)