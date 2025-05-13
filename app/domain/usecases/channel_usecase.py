from domain.usecases.services.query_service import QueryService
from domain.repositories.postgres_repository import PostgresRepository

class ChannelUsecase:

    __init_db: bool
    __do_indexing: bool
    __query_service: QueryService
    __postgres_repository: PostgresRepository

    def __init__(
        self,
        query_service: QueryService,
        postgres_repository: PostgresRepository
    ):
        self.__init_db = True
        self.__do_indexing = True
        self.__query_service = query_service
        self.__postgres_repository = postgres_repository

    async def submit_query(self, query: str) -> str:
        
        if self.__init_db:
            self.__postgres_repository.create_db()
            self.__init_db = False

        url = self.__postgres_repository.make_url()
        print(f"url : {str(url)}")
        vector_store = self.__query_service.get_vector_store(url)

        if self.__do_indexing:
            self.__query_service.index_data(vector_store=vector_store)
            self.__do_indexing = False
        
        return self.__query_service.query(vector_store, query)