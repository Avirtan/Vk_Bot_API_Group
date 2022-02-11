import asyncio
import aiohttp

from src.Vk_base import Vk_base

from .BotEventGroup import BotEventGroup


class VK_Bot:
    """
    Класс для получения событий сообщества с сервера вк
    Подробнее https://dev.vk.com/api/bots-long-poll/getting-started
    """
    vk: Vk_base = None
    __server = ""
    __key = ""
    __ts = ""
    __wait = 25

    def __init__(self, idGroup: str) -> None:
        self.idGroup = idGroup

    async def getLongPollServer(self):
        params = {
            "access_token": self.vk.accessKeyGroup,
            "lp_version":"3",
            "group_id": self.idGroup,
            "v": self.vk.versionApi
        }
        async with self.vk.session.get('https://api.vk.com/method/groups.getLongPollServer', params=params) as resp:
            json = await resp.json()
            self.__server = json["response"]["server"]
            self.__key = json["response"]["key"]
            self.__ts = json["response"]["ts"]

    async def get_event(self):
        if self.__server == "":
            await self.getLongPollServer()
        params = {
            "act": "a_check",
            "key": self.__key,
            "ts": self.__ts,
            "wait": self.__wait,
        }
        async with self.vk.session.get(url=self.__server, params=params) as resp:
            data = await resp.json()
            if 'failed' not in data:
                self.__ts = data['ts']
                return [
                    self.check_event(event) for event in data['updates']
                ]
            elif data['failed'] == 1:
                self.__ts = data['ts']
            elif data['failed'] == 2 or data['failed'] == 3:
                await self.getLongPollServer()
        return [BotEventGroup.EVENT_ERROR, {}]

    def check_event(self, data):
        if data == []:
            return [BotEventGroup.EVENT_EMPTY, {}]
        print(data["type"])
        event = BotEventGroup(data["type"])
        return [event, data]

    async def listen(self):
        while True:
            data = await self.get_event()
            for event in data:
                yield event
