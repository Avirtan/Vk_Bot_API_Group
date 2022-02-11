from src.Vk_base import Vk_base
import random

class HandlerHttp:
    """
    Класс для отправки запросов
    """
    @staticmethod
    async def get(method:str, params:dict, vk:Vk_base, url="https://api.vk.com/method/", isUser:bool = False):
        params["access_token"] = vk.accessKeyUser if isUser else vk.accessKeyGroup
        params["v"] = vk.versionApi
        params["random_id"] = random.randint(0,214748364)
        async with vk.session.get(url+method,params=params) as response:
            return await response.json() 