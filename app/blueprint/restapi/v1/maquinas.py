from flask.views import MethodView
from flask_smorest import Blueprint
from service.maquinas_service import MaquinasService, MaquinasPaginadoOutputModel

from dependency_injector.wiring import inject, Provide
from ext.dependency_injector import Container

blp = Blueprint("maquinas", "maquinas", url_prefix="/maquinas", description="Dados das maquinas")

@blp.route("/")
class Maquinas(MethodView):

    @inject
    def __init__(
            self,
            maquinas_service: MaquinasService = Provide[Container.maquinas_service]):
        self.maquinas_service = maquinas_service
        super().__init__()

    @blp.paginate()
    @blp.alt_response(200, schema=MaquinasPaginadoOutputModel)
    def get(self, pagination_parameters):
        return self.maquinas_service.listar(pagination_parameters.page_size, pagination_parameters.page)