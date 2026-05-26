from .base_repository import BaseRepo
from models.models import Hardware

class MaquinasRepo(BaseRepo):
    def __init__(self):
        super().__init__(Hardware)