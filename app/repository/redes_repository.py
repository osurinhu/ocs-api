from .base_repository import BaseRepo
from models.models import Networks

class RedesRepo(BaseRepo):
    def __init__(self):
        super().__init__(Networks)