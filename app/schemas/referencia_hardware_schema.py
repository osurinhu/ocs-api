from marshmallow import Schema, fields

class ReferenciaHardwareSchema(Schema):
    id = fields.Int(attribute='ID')
    nome = fields.String(attribute='NAME')