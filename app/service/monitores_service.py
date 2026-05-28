from marshmallow import Schema, fields
from schemas.paginacao_schema import PaginadoOutputModel

class MonitorOutputModel(Schema):
    id_computador = fields.Int(attribute='hardware.ID')
    computador = fields.String(attribute='hardware.NAME')

    id = fields.Int(attribute='ID')
    fabricante = fields.String(attribute='MANUFACTURER')
    modelo = fields.String(attribute='CAPTION')
    descricao = fields.String(attribute='DESCRIPTION')
    tipo = fields.String(attribute='TYPE')
    serial = fields.String(attribute='SERIAL')

class MonitoresPaginadoOutputModel(PaginadoOutputModel):
        items = fields.List(fields.Nested(MonitorOutputModel))

class MonitoresService:
    def __init__(self, monitores_repository):
        self.monitores_repository = monitores_repository
        super().__init__()

    def listar(self, per_page:int, page:int):
        result = self.monitores_repository.listar_paginado(page=page, per_page=per_page)
        return MonitoresPaginadoOutputModel().dump(result)
