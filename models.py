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