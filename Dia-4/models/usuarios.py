from config import conexion
from sqlalchemy import Column, types

class UsuarioModel(conexion.Model):

    __tablename__ = 'usuarios'

    id = Column(type_=types.Integer,autoincrement=True,primary_key=True)
    nombre = Column(type_=types.String(length=45))
    correo = Column(type_=types.String(length=45),unique=True ,nullable= False)
    telefono = Column(type_=types.String(length=15))