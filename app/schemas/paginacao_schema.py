from marshmallow import Schema, fields

class PaginadoOutputModel(Schema):
        page = fields.Int()
        per_page = fields.Int()
        total = fields.Int()
        has_next = fields.Bool()