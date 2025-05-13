from abc import ABC, abstractmethod
from typing import Any

class PostgresRepository(ABC):

    @abstractmethod
    def create_db(db_name: str):
        pass
    
    @abstractmethod
    def make_url(connection_string: str) -> Any:
        pass