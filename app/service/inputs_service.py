from marshmallow import Schema, fields
from schemas.referencia_hardware_schema import ReferenciaHardwareSchema
from schemas.paginacao_schema import PaginadoOutputModel

class InputOutputModel(Schema):
    hardware = fields.Nested(ReferenciaHardwareSchema)

    id = fields.Int(attribute='ID')
    tipo = fields.String(attribute='TYPE')
    fabricante = fields.String(attribute='MANUFACTURER')
    modelo = fields.String(attribute='CAPTION')
    descricao = fields.String(attribute='DESCRIPTION')
    interface = fields.String(attribute='INTERFACE')
    tipo_ponteiro = fields.String(attribute='POINTTYPE')

class InputsPaginadoOutputModel(PaginadoOutputModel):
        items = fields.List(fields.Nested(InputOutputModel))

class InputsService:
    def __init__(self, inputs_repository):
        self.inputs_repository = inputs_repository
        super().__init__()

    def listar(self, per_page:int, page:int):
        result = self.inputs_repository.listar_paginado(page=page, per_page=per_page)
        return InputsPaginadoOutputModel().dump(result)
