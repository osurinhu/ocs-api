from .base_repository import BaseRepo
from models.models import Drives

class DiscosRepo(BaseRepo):
    def __init__(self):
        super().__init__(Drives)