from .base_repository import BaseRepo
from models.models import Drives

class DrivesRepo(BaseRepo):
    def __init__(self):
        super().__init__(Drives)