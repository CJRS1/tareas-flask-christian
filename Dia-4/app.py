from flask import Flask
from config import conexion
from flask_migrate import Migrate
from os import environ
from dotenv import load_dotenv
from flask_restful import Api

from models.usuarios import UsuarioModel
from models.tareas import TareaModel
from controllers.usuarioController import UsuarioController
from controllers.pruebaController import PruebaController
from controllers.usuarioController import UsuarioController2
from controllers.tareaController import TareaController
from controllers.tareaController import TareaController2

load_dotenv()

app = Flask(__name__)

api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
conexion.init_app(app)

app.config['SQLALCHEMY_ECHO']=environ.get('MOSTRAR_SQL')

migrate = Migrate(app,conexion)

api.add_resource(UsuarioController, '/usuarios')
api.add_resource(PruebaController, '/prueba')
api.add_resource(UsuarioController2, '/usuarios/<int:id>')
api.add_resource(TareaController, '/tareas')
api.add_resource(TareaController2, '/tarea/<int:usuarioId>')

if __name__ == '__main__':
    app.run(debug=True)