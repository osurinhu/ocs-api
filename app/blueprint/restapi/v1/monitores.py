from flask.views import MethodView
from flask_smorest import Blueprint
from service.monitores_service import MonitoresService, MonitoresPaginadoOutputModel

from dependency_injector.wiring import inject, Provide
from ext.dependency_injector import Container

blp = Blueprint("monitores", "monitores", url_prefix="/monitores", description="Dados de monitores")

@blp.route("/")
class Monitores(MethodView):

    @inject
    def __init__(
            self,
            monitores_service: MonitoresService = Provide[Container.monitores_service]):
        self.monitores_service = monitores_service
        super().__init__()

    @blp.paginate()
    @blp.alt_response(200, schema=MonitoresPaginadoOutputModel)
    def get(self, pagination_parameters):
        return self.monitores_service.listar(pagination_parameters.page_size, pagination_parameters.page)