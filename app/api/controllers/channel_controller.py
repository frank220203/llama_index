from fastapi import Depends
from fastapi_utils.cbv import cbv

from api.deps.di_manager import get_channel_usecase
from api.dtos.channel_dto import ChannelDTO
from api.routes.base_routes import channel_router

from domain.usecases.channel_usecase import ChannelUsecase

@cbv(channel_router)
class ChannelController:
    
    @channel_router.post("/{channel_id}")
    async def submit_query(
        channel: ChannelDTO,
        channel_id: str,
        channel_usecase: ChannelUsecase = Depends(get_channel_usecase)
    ) -> str:
        """
        Gemini한테 질문하기
        """

        return channel_usecase.submit_query(channel.query)

    def get_router(self):
        return channel_router