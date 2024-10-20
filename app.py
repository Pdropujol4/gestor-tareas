from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Bienvenido al gestor de tareas!"

if __name__ == '__main__':
    app.run(debug=True)