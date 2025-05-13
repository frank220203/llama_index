import pytest

from unittest.mock import MagicMock
from domain.usecases.channel_usecase import ChannelUsecase

# submit_query 단위 테스트
@pytest.mark.anyio
async def test_submit_query(mock_query_service: MagicMock, mock_vector_repository: MagicMock) -> None:
    # Given & Mock
    # mock_vector_repository.make_url = MagicMock()
    # mock_vector_repository.make_url.return_value = "이건 모킹인데"

    # When & Mocking
    channel_usecase = ChannelUsecase(mock_query_service, mock_vector_repository)
    answer = await channel_usecase.submit_query("되나?")

    # Then
    assert answer == "된다"