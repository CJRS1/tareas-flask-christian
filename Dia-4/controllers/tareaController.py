from flask_restful import Resource, request
from config import conexion
from dtos.tareaDto import TareaRequestDto
from models.tareas import TareaModel
from models.usuarios import UsuarioModel

class TareaController(Resource):
    def post(self):
        body = request.get_json()
        try:

            serializador =  TareaRequestDto()
            dataSerializada = serializador.load(body)
            

            usuarioEncontrado=conexion.session.query(UsuarioModel).filter_by(id=dataSerializada.get('usuarioId')).first()

            if usuarioEncontrado is None:
                raise Exception('Tarea no existe')


            nuevaTarea=TareaModel(**dataSerializada)
            conexion.session.add(nuevaTarea)

            conexion.session.commit()
        
            # print(body)
            return{
                'message':'Yo soy el post de la tarea',
            }
        except Exception as error:
            print(error)
            return{
                'message':'Error al crear usuario'
            }
class TareaController2(Resource):
    def get(self,usuarioId):
        tareasEncontradas=conexion.session.query(TareaModel).filter_by(usuarioId=usuarioId).all()
        serializador=TareaRequestDto(many=True)

        data=serializador.dump(tareasEncontradas)
        return{
            'message':'Las tareas son',
            'content': data
        }