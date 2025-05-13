import pytest
from unittest.mock import MagicMock
from core.repositories.postgres_repository_impl import PostgresRepositoryImpl

@pytest.fixture(scope="module")
def mock_query_service() -> MagicMock:
    mock_query_service = MagicMock()
    return mock_query_service

@pytest.fixture(scope="module")
def mock_vector_repository() -> MagicMock:
    mock_vector_repository = MagicMock()
    mock_vector_repository = PostgresRepositoryImpl()
    return mock_vector_repository