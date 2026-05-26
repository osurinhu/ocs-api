from dependency_injector.wiring import Provide, inject
from sqlalchemy import select
from models.models import Hardware
from marshmallow import Schema, fields

class BiosOutputModel(Schema):
    fabricante = fields.String(attribute='SMANUFACTURER')
    modelo = fields.String(attribute='SMODEL')
    serial = fields.String(attribute='SSN')
    data_bios = fields.String(attribute='BDATE')

class HardwareOutputModel(Schema):
    id = fields.Int(attribute='ID')
    computador = fields.String(attribute='NAME')
    ip = fields.String(attribute='IPADDR')

    sistema = fields.String(attribute='OSNAME')
    versao_so = fields.String(attribute='OSVERSION')

    ram_mb = fields.Int(attribute='MEMORY')
    usuario = fields.String(attribute='USERID')

    ultimo_inventario = fields.DateTime(attribute='LASTDATE')
    bios = fields.Nested(BiosOutputModel)

class MaquinasPaginadoOutputModel(Schema):
    items = fields.List(fields.Nested(HardwareOutputModel))
    page = fields.Int()
    per_page = fields.Int()
    total = fields.Int()
    has_next = fields.Bool()

class MaquinasService:
    def __init__(self, maquinas_repository):
        self.maquinas_repository = maquinas_repository
        super().__init__()


    def listar(self, per_page:int, page:int):
        query = (select(Hardware))

        result = self.maquinas_repository.listar_paginado(page=page, per_page=per_page)

        return MaquinasPaginadoOutputModel().dump(result)