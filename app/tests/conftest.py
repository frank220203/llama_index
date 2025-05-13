import pytest
from unittest.mock import MagicMock
from core.repositories.vector_repository_impl import VectorRepositoryImpl

@pytest.fixture(scope="module")
def mock_query_service() -> MagicMock:
    mock_query_service = MagicMock()
    return mock_query_service

@pytest.fixture(scope="module")
def mock_vector_repository() -> MagicMock:
    mock_vector_repository = MagicMock()
    mock_vector_repository = VectorRepositoryImpl()
    return mock_vector_repository