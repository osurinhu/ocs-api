from flask_smorest import Api, Blueprint
from ext.config import load_routes

spec = {
    'title':'API',
    'version':'V1',
    'openapi_version':"3.0.2"}

api = Api(spec_kwargs=spec)

blp = Blueprint('v1', __name__, url_prefix='/api/v1')

def init_app(app):
    api.init_app(app)
    load_routes(app, api, blp)
