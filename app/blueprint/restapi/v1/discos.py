from flask.views import MethodView
from flask_smorest import Blueprint
from service.discos_service import DiscosService, DiscosPaginadoOutputModel

from dependency_injector.wiring import inject, Provide
from ext.dependency_injector import Container

blp = Blueprint("discos", "discos", url_prefix="/discos", description="Dados de discos")

@blp.route("/")
class Discos(MethodView):

    @inject
    def __init__(
            self,
            discos_service: DiscosService = Provide[Container.discos_service]):
        self.discos_service = discos_service
        super().__init__()

    @blp.paginate()
    @blp.alt_response(200, schema=DiscosPaginadoOutputModel)
    def get(self, pagination_parameters):
        return self.discos_service.listar(pagination_parameters.page_size, pagination_parameters.page)