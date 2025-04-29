from fastapi_utils.cbv import cbv
from api.dtos.channel_dto import ChannelDTO
from api.routes.base_routes import channel_router

@cbv(channel_router)
class ChannelController:
    
    @channel_router.post("/{channel_id}")
    async def submit_query(
        channel_id: str,
        channel: ChannelDTO
    ) -> str:
        """
        Gemini한테 질문하기
        """

        return channel.query

    def get_router(self):
        return channel_router