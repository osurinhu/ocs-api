from .base_repository import BaseRepo
from models.models import Inputs

class InputsRepo(BaseRepo):
    def __init__(self):
        super().__init__(Inputs)