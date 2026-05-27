from dependency_injector import containers, providers

from service.maquinas_service import MaquinasService
from service.softwares_service import SoftwaresService
from service.drives_service import DrivesService
from service.redes_service import RedesService
from service.processadores_service import ProcessadoresService

from repository.maquinas_repository import MaquinasRepo
from repository.softwares_repository import SoftwaresRepo
from repository.drives_repository import DrivesRepo
from repository.redes_repository import RedesRepo
from repository.processadores_repository import ProcessadoresRepo

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["blueprint.restapi.v1", "service"])
    
    maquinas_repository = providers.Factory(
        MaquinasRepo
    )
    softwares_repository = providers.Factory(
        SoftwaresRepo
    )
    drives_repository = providers.Factory(
        DrivesRepo
    )
    redes_repository = providers.Factory(
        RedesRepo
    )
    processadores_repository = providers.Factory(
        ProcessadoresRepo
    )

    maquinas_service = providers.Factory(
        MaquinasService,
        maquinas_repository=maquinas_repository
    )
    softwares_service = providers.Factory(
        SoftwaresService,
        softwares_repository=softwares_repository
    )
    drives_service = providers.Factory(
        DrivesService,
        drives_repository=drives_repository
    )
    redes_service = providers.Factory(
        RedesService,
        redes_repository=redes_repository
    )
    processadores_service = providers.Factory(
        ProcessadoresService,
        processadores_repository=processadores_repository
    )

def init_app(app):
    container = Container()
    app.container = container