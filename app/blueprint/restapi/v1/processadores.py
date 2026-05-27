from flask.views import MethodView
from flask_smorest import Blueprint
from service.processadores_service import ProcessadoresService, ProcessadoresPaginadoOutputModel

from dependency_injector.wiring import inject, Provide
from ext.dependency_injector import Container

blp = Blueprint("processadores", "processadores", url_prefix="/processadores", description="Dados de processadores")

@blp.route("/")
class Processadores(MethodView):

    @inject
    def __init__(
            self,
            processadores_service: ProcessadoresService = Provide[Container.processadores_service]):
        self.processadores_service = processadores_service
        super().__init__()

    @blp.paginate()
    @blp.alt_response(200, schema=ProcessadoresPaginadoOutputModel)
    def get(self, pagination_parameters):
        return self.processadores_service.listar(pagination_parameters.page_size, pagination_parameters.page)