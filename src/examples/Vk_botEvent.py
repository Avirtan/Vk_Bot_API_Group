import aiohttp
import asyncio
from src.Vk_Bot import VK_Bot
from src.BotEventGroup import BotEventGroup

accessKeyGroup = "access_tokenGroup"
accessKeyUser = "access_tokenUser"
idGroup = "1234566"

"""
    Простой бот который отслеживает события нового сообщения и событие написания сообщения
    Создаётся класса для бота, которые обрабатывает события с сервера. Исользуется Bots Long Poll API 
    Подробнее https://dev.vk.com/api/bots-long-poll/getting-started
"""
if __name__ == '__main__':
    async def main():
        async with aiohttp.ClientSession() as session:
            bot = VK_Bot(accessKeyGroup=accessKeyGroup,
                         session=session, idGroup=idGroup)
            """
            в data[0] хранит BotEventGroup,
            в data[1] данные с сервера
            """
            async for data in bot.listen():
                if data[0] == BotEventGroup.MESSAGE_NEW:
                    print("message_new")
                if data[0] == BotEventGroup.MESSAGE_TYPING:
                    print("typing message")
    asyncio.run(main())
