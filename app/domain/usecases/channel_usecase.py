from domain.usecases.services.query_service import QueryService
from domain.repositories.vector_repository import VectorRepository

class ChannelUsecase:

    __init_db: bool
    __do_indexing: bool
    __query_service: QueryService
    __vector_repository: VectorRepository

    def __init__(
        self,
        query_service: QueryService,
        vector_repository: VectorRepository
    ):
        self.__init_db = True
        self.__do_indexing = True
        self.__query_service = query_service
        self.__vector_repository = vector_repository

    async def submit_query(self, query: str) -> str:
        
        if self.__init_db:
            self.__vector_repository.create_vector_db()
            self.__init_db = False

        url = self.__vector_repository.make_url()
        print(f"url : {str(url)}")
        vector_store = self.__query_service.get_vector_store(url)

        if self.__do_indexing:
            self.__query_service.index_data(vector_store=vector_store)
            self.__do_indexing = False
        
        return self.__query_service.query(vector_store, query)