from src.Vk_base import Vk_base
from src.Handlers.HandlerHttp import HandlerHttp


class MessageApi:
    """
    Класс для работы с методами сообщений
    Подробнее https://dev.vk.com/method/messages
    """
    vk:Vk_base = None

    @staticmethod
    async def send(params: dict):
        await HandlerHttp.get(method="messages.send",
                        params=params, vk=MessageApi.vk)
    
    @staticmethod
    async def sendMessageEventAnswer(params: dict):
        await HandlerHttp.get(method="messages.sendMessageEventAnswer",
                        params=params, vk=MessageApi.vk)

