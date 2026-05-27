from flask.views import MethodView
from flask_smorest import Blueprint
from service.redes_service import RedesService, RedesPaginadoOutputModel

from dependency_injector.wiring import inject, Provide
from ext.dependency_injector import Container

blp = Blueprint("redes", "redes", url_prefix="/redes", description="Dados de redes")

@blp.route("/")
class Redes(MethodView):

    @inject
    def __init__(
            self,
            redes_service: RedesService = Provide[Container.redes_service]):
        self.redes_service = redes_service
        super().__init__()

    @blp.paginate()
    @blp.alt_response(200, schema=RedesPaginadoOutputModel)
    def get(self, pagination_parameters):
        return self.redes_service.listar(pagination_parameters.page_size, pagination_parameters.page)