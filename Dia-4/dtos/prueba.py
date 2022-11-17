from marshmallow import Schema, fields

class PruebaDto(Schema):
    id=fields.Int()
    nombre=fields.Str(required=True, error_messages={'required':'Este campo es obligatorio'})
    correo= fields.Email(error_messages={'invalid':'Correo electronico invalido'})