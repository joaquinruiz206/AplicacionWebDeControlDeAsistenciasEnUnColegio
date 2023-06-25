from __main__ import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

class Curso(db.Model):
    __tablename__="curso"
    id= db.Column(db.Integer, primary_key=True)
    anio=db.Column(db.Integer, nullable=False)
    division=db.Column(db.Integer, nullable=False)
    idpreceptor=db.Column(db.Integer, db.ForeignKey("preceptor.id"))
    estudiantes=db.relationship('Estudiante',backref='curso', cascade="all")

class Preceptor(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(40),nullable=False)
    apellido=db.Column(db.String(40),nullable=False)
    correo=db.Column(db.String(40),unique=True, nullable=False)
    clave=db.Column(db.String(120),nullable=False)
    cursos=db.relationship('Curso',backref='preceptor', cascade="all")
    


class Estudiante(db.Model): 
    __tablename__ = "estudiante"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(40), nullable = False)
    apellido = db.Column(db.String(40), nullable = False)
    dni = db.Column(db.String(20), nullable = False)
    idcurso = db.Column(db.Integer, nullable = False)
    idpadre = db.Column(db.Integer, nullable = False)
    idcurso=db.Column(db.Integer, db.ForeignKey("curso.id"))
    asistencias=db.relationship('Asistencia',backref='estudiante', cascade="all")
    idpadre=db.Column(db.Integer, db.ForeignKey("padre.id"))
    def __lt__(self,otro):
        if self.nombre == otro.nombre:    
            return self.apellido < otro.apellido
        else:
            return self.nombre < otro.nombre
        
        

class Asistencia(db.Model):
    __tablename__ = "asistencia"
    id = db.Column(db.Integer, primary_key = True)
    fecha = db.Column(db.DateTime, nullable = False)
    codigoclase = db.Column(db.Integer, nullable = False)
    asistio = db.Column(db.String(1), nullable = False)
    justificacion = db.Column(db.Text, nullable = False)
    idestudiante = db.Column(db.Integer, nullable = False)
    idestudiante=db.Column(db.Integer, db.ForeignKey("estudiante.id"))

    


class Padre(db.Model):
    __tablename__ = "padre"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(40), nullable = False)
    apellido = db.Column(db.String(40), nullable = False)
    correo = db.Column(db.String(50), unique = True, nullable = False)
    clave = db.Column(db.String(120),unique = True, nullable = False)
    hijos=db.relationship('Estudiante',backref='padre', cascade="all")
