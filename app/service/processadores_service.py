from marshmallow import Schema, fields
from schemas.referencia_hardware_schema import ReferenciaHardwareSchema
from schemas.paginacao_schema import PaginadoOutputModel

class ProcessadorOutputModel(Schema):
    hardware = fields.Nested(ReferenciaHardwareSchema)

    id = fields.Int(attribute='ID')
    processador = fields.String(attribute='TYPE')
    fabricante = fields.String(attribute='MANUFACTURER')
    mhz = fields.String(attribute='SPEED')
    nucleos = fields.Int(attribute='CORES')
    nucleos_logicos = fields.Int(attribute='LOGICAL_CPUS')
    arquitetura = fields.String(attribute='CPUARCH')

class ProcessadoresPaginadoOutputModel(PaginadoOutputModel):
        items = fields.List(fields.Nested(ProcessadorOutputModel))

class ProcessadoresService:
    def __init__(self, processadores_repository):
        self.processadores_repository = processadores_repository
        super().__init__()

    def listar(self, per_page:int, page:int):
        result = self.processadores_repository.listar_paginado(page=page, per_page=per_page)
        return ProcessadoresPaginadoOutputModel().dump(result)
