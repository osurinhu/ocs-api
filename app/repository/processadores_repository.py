from .base_repository import BaseRepo
from models.models import Cpus

class ProcessadoresRepo(BaseRepo):
    def __init__(self):
        super().__init__(Cpus)