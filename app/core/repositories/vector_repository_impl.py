from sqlalchemy import URL
from sqlalchemy import create_engine, text

from core.configs.app_config import Settings
from domain.repositories.vector_repository import VectorRepository

class VectorRepositoryImpl(VectorRepository):

    __settings = Settings()
    __connestion_string = __settings.SQLALCHEMY_DATABASE_URI

    def create_vector_db(self, connection_string: str = "", db_name: str = __settings.VECTOR_DB):
        connection_string = str(self.__connestion_string) + "/" + self.__settings.POSTGRE_DB
        conn = create_engine(connection_string)
        with conn.connect() as c:
            c.execution_options(isolation_level="AUTOCOMMIT")
            c.execute(text(f"DROP DATABASE IF EXISTS {db_name}"))
            c.execute(text(f"CREATE DATABASE {db_name}"))
    
    def make_url(connection_string: str = __settings.SQLALCHEMY_DATABASE_URI) -> URL:
        return connection_string