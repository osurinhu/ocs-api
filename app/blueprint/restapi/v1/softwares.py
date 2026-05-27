from flask.views import MethodView
from flask_smorest import Blueprint
from service.softwares_service import SoftwaresService, SoftwaresPaginadoOutputModel

from dependency_injector.wiring import inject, Provide
from ext.dependency_injector import Container

blp = Blueprint("softwares", "softwares", url_prefix="/softwares", description="Dados de softwares")

@blp.route("/")
class Softwares(MethodView):

    @inject
    def __init__(
            self,
            softwares_service: SoftwaresService = Provide[Container.softwares_service]):
        self.softwares_service = softwares_service
        super().__init__()

    @blp.paginate()
    @blp.alt_response(200, schema=SoftwaresPaginadoOutputModel)
    def get(self, pagination_parameters):
        return self.softwares_service.listar(pagination_parameters.page_size, pagination_parameters.page)