from dependency_injector import containers, providers

from service.maquinas_service import MaquinasService
from service.softwares_service import SoftwaresService
from service.discos_service import DiscosService
from service.redes_service import RedesService
from service.processadores_service import ProcessadoresService
from service.monitores_service import MonitoresService
from service.inputs_service import InputsService

from repository.maquinas_repository import MaquinasRepo
from repository.softwares_repository import SoftwaresRepo
from repository.discos_repository import DiscosRepo
from repository.redes_repository import RedesRepo
from repository.processadores_repository import ProcessadoresRepo
from repository.monitores_repository import MonitoresRepo
from repository.processadores_repository import ProcessadoresRepo
from repository.inputs_repository import InputsRepo

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["blueprint.restapi.v1", "service"])
    
    # Repositorios

    maquinas_repository = providers.Factory(
        MaquinasRepo
    )
    softwares_repository = providers.Factory(
        SoftwaresRepo
    )
    discos_repository = providers.Factory(
        DiscosRepo
    )
    redes_repository = providers.Factory(
        RedesRepo
    )
    processadores_repository = providers.Factory(
        ProcessadoresRepo
    )
    monitores_repository = providers.Factory(
        MonitoresRepo
    )
    inputs_repository = providers.Factory(
        InputsRepo
    )

    # Services

    maquinas_service = providers.Factory(
        MaquinasService,
        maquinas_repository=maquinas_repository
    )
    softwares_service = providers.Factory(
        SoftwaresService,
        softwares_repository=softwares_repository
    )
    discos_service = providers.Factory(
        DiscosService,
        discos_repository=discos_repository
    )
    redes_service = providers.Factory(
        RedesService,
        redes_repository=redes_repository
    )
    processadores_service = providers.Factory(
        ProcessadoresService,
        processadores_repository=processadores_repository
    )
    monitores_service = providers.Factory(
        MonitoresService,
        monitores_repository=monitores_repository
    )
    inputs_service = providers.Factory(
        InputsService,
        inputs_repository=inputs_repository
    )

def init_app(app):
    container = Container()
    app.container = container