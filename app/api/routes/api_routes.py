from fastapi import APIRouter

from api.controllers.channel_controller import ChannelController

class ApiRoutes:
    
    __router: APIRouter
    __channelController: ChannelController
    
    def __init__(self):
        self.__router = APIRouter()
        self.__channelController = ChannelController()
        self.__router.include_router(self.__channelController.get_router())
    
    def get_router(self):
        return self.__router