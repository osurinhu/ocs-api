from marshmallow import Schema, fields
from schemas.paginacao_schema import PaginadoOutputModel

class DriveOutputModel(Schema):
    id_computador = fields.Int(attribute='ID')
    computador = fields.String(attribute='hardware.NAME')

    volume = fields.String(attribute='VOLUMN')
    total_mb = fields.Int(attribute='TOTAL')
    livre_mb = fields.Int(attribute='FREE')
    ocupado_mb = fields.Int()

class DrivesPaginadoOutputModel(PaginadoOutputModel):
        items = fields.List(fields.Nested(DriveOutputModel))

class DrivesService:
    def __init__(self, drives_repository):
        self.drives_repository = drives_repository
        super().__init__()


    def listar(self, per_page:int, page:int):
        result = self.drives_repository.listar_paginado(page=page, per_page=per_page)
        return DrivesPaginadoOutputModel().dump(result)
