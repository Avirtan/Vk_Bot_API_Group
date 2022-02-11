from src.Handlers.HandlerHttp import HandlerHttp
from src.MethodsApi.MessageApi import MessageApi
from src.Vk_base import Vk_base

class WallApi:
    """
    Класс для работы с записями на стене
    Подробнее https://dev.vk.com/method/wall
    """
    vk:Vk_base = None

    @staticmethod
    async def get(params: dict):
        return await HandlerHttp.get(method="wall.get",
                        params=params, vk=WallApi.vk, isUser=True)

    @staticmethod
    async def post(params: dict):
        return await HandlerHttp.get(method="wall.post",
                        params=params, vk=WallApi.vk, isUser=True)
    