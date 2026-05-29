from marshmallow import Schema, fields
from schemas.referencia_hardware_schema import ReferenciaHardwareSchema
from schemas.paginacao_schema import PaginadoOutputModel

class RedeOutputModel(Schema):
    hardware = fields.Nested(ReferenciaHardwareSchema)

    id = fields.Int(attribute='ID')
    ip = fields.String(attribute='IPADDRESS')
    mac = fields.String(attribute='MACADDR')
    interface = fields.String(attribute='DESCRIPTION')

class RedesPaginadoOutputModel(PaginadoOutputModel):
        items = fields.List(fields.Nested(RedeOutputModel))

class RedesService:
    def __init__(self, redes_repository):
        self.redes_repository = redes_repository
        super().__init__()

    def listar(self, per_page:int, page:int):
        result = self.redes_repository.listar_paginado(page=page, per_page=per_page)
        return RedesPaginadoOutputModel().dump(result)
