from dependency_injector import containers, providers

from service.maquinas_service import MaquinasService

from repository.maquinas_repository import MaquinasRepo

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["blueprint.restapi.v1", "service"])
    
    maquinas_repository = providers.Factory(
        MaquinasRepo
    )

    maquinas_service = providers.Factory(
        MaquinasService,
        maquinas_repository=maquinas_repository
    )

def init_app(app):
    container = Container()
    app.container = container