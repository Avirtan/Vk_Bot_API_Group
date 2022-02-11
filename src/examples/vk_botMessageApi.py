import aiohttp
import asyncio
from src.MethodsApi.MessageApi import MessageApi
from src.Objects.Message import Message_new, Message_typing
from src.Vk_Bot import VK_Bot
from src.BotEventGroup import BotEventGroup
from src.Vk_base import Vk_base

accessKeyGroup = "access_tokenGroup"
accessKeyUser = "access_tokenUser"
idGroup = "1234566"

"""
Создаётся 2 класса
VK_Bot для прослушивания событий с сервера вк
Vk_base для хранения токенов и сессии, используется в методах апи 
MessageApi содержит методы для работы с личными сообщениями
"""
if __name__ == '__main__':
    async def main():
        async with aiohttp.ClientSession() as session:
            bot = VK_Bot(accessKeyGroup=accessKeyGroup,
                         session=session, idGroup=idGroup)
            VK = Vk_base(accessKeyGroup=accessKeyGroup,
                         accessKeyUser=accessKeyUser, session=session)
            MessageApi.vk = VK
            """
            в data[0] хранится BotEventGroup,
            в data[1] данные с сервера
            """
            async for data in bot.listen():
                if data[0] == BotEventGroup.MESSAGE_NEW:
                    message_new: Message_new = Message_new(data[1])
                    if message_new.text == "Help":
                        params = {
                            "user_id": message_new.from_id,
                            "peer_id": message_new.from_id,
                            "message": "Чем помочь?",
                        }
                        await MessageApi.send(params=params)
                if data[0] == BotEventGroup.MESSAGE_TYPING:
                    message_typing = Message_typing(data[1])
                    params = {
                        "user_id": message_typing.from_id,
                        "peer_id": message_typing.from_id,
                        "message": "что пишем",
                    }
                    await MessageApi.send(params=params)
    asyncio.run(main())
