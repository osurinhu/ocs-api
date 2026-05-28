from marshmallow import Schema, fields
from schemas.paginacao_schema import PaginadoOutputModel

class DiscoOutputModel(Schema):
    id_computador = fields.Int(attribute='hardware.ID')
    computador = fields.String(attribute='hardware.NAME')

    id = fields.Int(attribute='ID')
    volume = fields.String(attribute='VOLUMN')
    total_mb = fields.Int(attribute='TOTAL')
    livre_mb = fields.Int(attribute='FREE')
    ocupado_mb = fields.Method('calcular_espaco_ocupado')

    def calcular_espaco_ocupado(self, obj):
        return obj.TOTAL - obj.FREE

class DiscosPaginadoOutputModel(PaginadoOutputModel):
        items = fields.List(fields.Nested(DiscoOutputModel))

class DiscosService:
    def __init__(self, discos_repository):
        self.discos_repository = discos_repository
        super().__init__()


    def listar(self, per_page:int, page:int):
        result = self.discos_repository.listar_paginado(page=page, per_page=per_page)
        return DiscosPaginadoOutputModel().dump(result)
