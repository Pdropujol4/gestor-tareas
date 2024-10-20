from flask import Flask, render_template, request, redirect, url_for
from models import db, Usuario, Tarea  # Importamos nuestros modelos desde models.py

app = Flask(__name__)

# Configuración de la base de datos
app.config['SECRET_KEY'] = 'mi_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para agregar un usuario
@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = Usuario(nombre=nombre)
        db.session.add(usuario)
        db.session.commit()
        return redirect(url_for('ver_usuarios'))
    return render_template('agregar_usuario.html')

# Ruta para ver usuarios y sus tareas
@app.route('/usuarios')
def ver_usuarios():
    usuarios = Usuario.query.all()  # Consultar todos los usuarios
    return render_template('usuarios.html', usuarios=usuarios)

# Ruta para agregar una tarea a un usuario
@app.route('/agregar_tarea/<int:usuario_id>', methods=['GET', 'POST'])
def agregar_tarea(usuario_id):
    usuario = Usuario.query.get_or_404(usuario_id)  # Obtener el usuario
    if request.method == 'POST':
        titulo = request.form['titulo']
        tarea = Tarea(titulo=titulo, autor=usuario)
        db.session.add(tarea)
        db.session.commit()
        return redirect(url_for('ver_usuarios'))
    return render_template('agregar_tarea.html', usuario=usuario)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear las tablas si no existen
    app.run(debug=True)