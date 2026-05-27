from marshmallow import Schema, fields
from schemas.paginacao_schema import PaginadoOutputModel

class SoftwareOutputModel(Schema):
    id_computador = fields.Int(attribute='ID')
    computador = fields.String(attribute='hardware.NAME')

    software = fields.String(attribute='software_name.NAME')
    versao = fields.String(attribute='software_version.VERSION')
    fabricante = fields.String(attribute='software_publisher.PUBLISHER')

class SoftwaresPaginadoOutputModel(PaginadoOutputModel):
        items = fields.List(fields.Nested(SoftwareOutputModel))

class SoftwaresService:
    def __init__(self, softwares_repository):
        self.softwares_repository = softwares_repository
        super().__init__()


    def listar(self, per_page:int, page:int):
        result = self.softwares_repository.listar_paginado(page=page, per_page=per_page)
        return SoftwaresPaginadoOutputModel().dump(result)
