from flask.views import MethodView
from flask_smorest import Blueprint
from service.drives_service import DrivesService, DrivesPaginadoOutputModel

from dependency_injector.wiring import inject, Provide
from ext.dependency_injector import Container

blp = Blueprint("drives", "drives", url_prefix="/drives", description="Dados de drives")

@blp.route("/")
class Drives(MethodView):

    @inject
    def __init__(
            self,
            drives_service: DrivesService = Provide[Container.drives_service]):
        self.drives_service = drives_service
        super().__init__()

    @blp.paginate()
    @blp.alt_response(200, schema=DrivesPaginadoOutputModel)
    def get(self, pagination_parameters):
        return self.drives_service.listar(pagination_parameters.page_size, pagination_parameters.page)