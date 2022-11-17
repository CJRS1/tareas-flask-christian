from flask_restful import Resource, request
from config import conexion
from models.usuarios import UsuarioModel
from dtos.usuarioDto import UsuarioRequestDto

class UsuarioController(Resource):
    def get(self):

        usuarios=conexion.session.query(UsuarioModel).all()
        print(usuarios)
        print(usuarios[0].nombre)

        serializador=UsuarioRequestDto(many=True)

        data = serializador.dump(usuarios)

        # usuariosFinales=[]

        # for usuario in usuarios:
            

        #     usuarioDiccionario={
        #         'id':usuario.id,
        #         'nombre':usuario.nombre,
        #         'correo':usuario.correo,
        #         'telefono':usuario.telefono

        #     }
        #     usuariosFinales.append(usuarioDiccionario)

        
        return{
            'message':'Yo soy el get del usuario',
            'content':  data
        }
    def post(self):
        body = request.get_json()
        try:

            serializador = UsuarioRequestDto()
            dataSerializada = serializador.load(body)
            print(dataSerializada)
            
            nuevoUsuario=UsuarioModel(**dataSerializada)

            # nuevoUsuario = UsuarioModel()
            # nuevoUsuario.correo = body.get('correo')
            # nuevoUsuario.nombre = body.get('nombre')
            # nuevoUsuario.telefono = body.get('telefono')
        
            conexion.session.add(nuevoUsuario)

            conexion.session.commit()
        
            # print(body)
            return{
                'message':'Yo soy el post del usuario'
            }
        except Exception as error:
            print(error)
            return{
                'message':'Error al crear usuario'
            }
class UsuarioController2(Resource):
    def get(self,id):

        usuarioEncontrado=conexion.session.query(UsuarioModel).filter_by(id=id).first()

        serializador=UsuarioRequestDto()
        data = serializador.dump(usuarioEncontrado)
        return{
            'message':'Yo soy el get del usuario',
            'content':  data
        }
    def put(self,id):
        try:
            usuarioEncontrado=conexion.session.query(UsuarioModel).filter_by(id=id).first()

            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')
            body=request.get_json()
            serializador=UsuarioRequestDto()
            data = serializador.dump(body)

            telefono = usuarioEncontrado.telefono

            try:
                telefono=data['telefono']
            except:
                pass

            usuarioEncontrado.nombre=data.get('nombre')
            usuarioEncontrado.correo=data.get('correo')
            usuarioEncontrado.telefono=telefono

            conexion.session.commit()
            
            return{
            'message':'Yo soy el get del usuario',
            'content':  data
            }
        except Exception as error:
            return{
                'message':'Error al acrtualizar el usuario',
                'content':error.args
            }
    def delete(self,id):
        try:
            usuarioEncontrado=conexion.session.query(UsuarioModel).filter_by(id=id).first()

            if usuarioEncontrado is None:
                raise Exception('Usuario no existe')

            conexion.session.delete(usuarioEncontrado)
            conexion.session.commit()
            
            return{
            'message':'Yo soy el delete del usuario',

            }
        except Exception as error:
            return{
                'message':'Error al eliminar el usuario',
                'content':error.args
            }