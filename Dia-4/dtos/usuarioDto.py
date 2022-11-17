from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.usuarios import UsuarioModel

class UsuarioRequestDto(SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel