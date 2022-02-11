import aiohttp
import asyncio
import webbrowser


class Vk_OAuth:
    """
    Класс на получение Access token Implicit Flow 
    Version Api 5.131
    Подробнее https://dev.vk.com/api/access-token/getting-started
    """
    __url: str = "https://oauth.vk.com/authorize"
    __version: str = "5.131"

    def __init__(self, session: aiohttp.ClientSession) -> None:
        self.session = session

    async def generateAccessLinkUser(self, clientId: str, scope: int):
        param = {
            "client_id": clientId,
            "display": "page",
            "redirect_uri": "https://oauth.vk.com/blank.html",
            "scope": str(scope),
            "response_type": "token",
            "v": self.__version
        }
        async with self.session.get(self.__url, params=param) as response:
            webbrowser.open_new_tab(str(response.url))

    async def generateAccessLinkGroup(self, clientId: str, group_ids: str, scope: int):
        param = {
            "client_id": clientId,
            "group_ids":group_ids,
            "display": "page",
            "redirect_uri": "https://oauth.vk.com/blank.html",
            "scope": str(scope),
            "response_type": "token",
            "v": self.__version
        }
        async with self.session.get(self.__url, params=param) as response:
            webbrowser.open_new_tab(str(response.url))
