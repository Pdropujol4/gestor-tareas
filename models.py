from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    tareas = db.relationship('Tarea', backref='autor', lazy=True)

    def __init__(self, nombre):
        self.nombre = nombre

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def __repr__(self):
        return f'Usuario({self.nombre})'

# Modelo de Tarea
class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    fecha_creacion = db.Column(db.DateTime, default=datetime.utcnow)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    def __init__(self, titulo):
        self.titulo = titulo

    def __repr__(self):
        return f'Tarea({self.titulo}, Completada: {self.fecha_creacion})'