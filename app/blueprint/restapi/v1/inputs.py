from flask.views import MethodView
from flask_smorest import Blueprint
from service.inputs_service import InputsService, InputsPaginadoOutputModel

from dependency_injector.wiring import inject, Provide
from ext.dependency_injector import Container

blp = Blueprint("inputs", "inputs", url_prefix="/inputs", description="Dados de inputs")

@blp.route("/")
class Inputs(MethodView):

    @inject
    def __init__(
            self,
            inputs_service: InputsService = Provide[Container.inputs_service]):
        self.inputs_service = inputs_service
        super().__init__()

    @blp.paginate()
    @blp.alt_response(200, schema=InputsPaginadoOutputModel)
    def get(self, pagination_parameters):
        return self.inputs_service.listar(pagination_parameters.page_size, pagination_parameters.page)