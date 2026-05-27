from .base_repository import BaseRepo
from models.models import Software

class SoftwaresRepo(BaseRepo):
    def __init__(self):
        super().__init__(Software)