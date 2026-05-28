from .base_repository import BaseRepo
from models.models import Monitors

class MonitoresRepo(BaseRepo):
    def __init__(self):
        super().__init__(Monitors)