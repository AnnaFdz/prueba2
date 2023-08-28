from flask import Flask
from config import Config
from flask import request, render_template, redirect
import csv

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    # Un endpoint que dice 'Hola Mundo!'
    @app.route('/')
    def hello_world():
        return 'Hola Mundo!'
    #return app
    @app.route('/academia')
    @app.route('/home')
    def bienvenida():
        return 'Bienvenido a Programacion 2!'
    @app.route('/help/')
    def help():
        return 'Soporte de la aplicación'
    @app.route('/about')
    def about():
        return 'Información acerca de la aplicación'
    @app.route('/perfil/<username>')
    def perfil(username):
        """Mensaje de bienvenida a un usuario"""
        return f'Bienvenido {username}!'
    # @app.route('/login', methods=['GET', 'POST'])
    # def login():
    #     if request.method == 'POST':
    #         return logearse()
    #     else:
    #         return mostrar_formulario()
    @app.post('/login')
    def login_post():
        return logearse()
    @app.get('/login')
    def login_get():
        return mostrar_formulario()
    
    def mostrar_formulario():
        return render_template('formulario_login.html')
    def logearse():
        usuarios = obtener_usuarios()
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        if usuarios.get(nombre) == contrasena:
           # return "Inicio de sesión exitoso"
           return redirect(f'/perfil/{nombre}')
        else:
            return "Error: Nombre de usuario o contraseña incorrectos"
        
    def obtener_usuarios():
        usuarios = {}
        with open('usuarios.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # Saltamos la primera fila (cabecera)
            for row in reader:
                usuarios[row[0]] = row[1]
        return usuarios

    return app
    
    
