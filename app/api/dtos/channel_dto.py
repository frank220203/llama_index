from pydantic import BaseModel, Field

class ChannelDTO(BaseModel):
    channel_id: str = Field(..., description="채널 ID")
    query: str = Field(..., description="질문 하세요")