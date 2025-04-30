from fastapi import Depends

from core.external_interfaces.query_service_impl import QueryServiceImpl
from core.repositories.vector_repository_impl import VectorRepositoryImpl

from domain.usecases.channel_usecase import ChannelUsecase
from domain.usecases.services.query_service import QueryService
from domain.repositories.vector_repository import VectorRepository

# fastapi는 의존성 부여를 endpoint에서 시작하고, 
# 함수 형태로만 의존성 부여를 하기 때문에 class가 아닌 일반 함수 사용

## Services
def get_query_service() -> QueryService:
    return QueryServiceImpl()

## Repositories
def get_vectore_repository() -> VectorRepository:
    return VectorRepositoryImpl()

## Usecases
def get_channel_usecase(query_service: QueryService = Depends(get_query_service), vector_repository: VectorRepository = Depends(get_vectore_repository)) -> ChannelUsecase:
    return ChannelUsecase(query_service, vector_repository)