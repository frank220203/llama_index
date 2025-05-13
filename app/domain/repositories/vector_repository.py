from abc import ABC, abstractmethod
from typing import Any

class VectorRepository(ABC):

    @abstractmethod
    def create_vector_db(connection_string: str, db_name: str):
        pass
    
    @abstractmethod
    def make_url(connection_string: str) -> Any:
        pass