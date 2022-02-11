import aiohttp
import asyncio
from src.Handlers.HandlerJson import HandlerJson
from src.Keyboard.Button import OpenLinkButton, TextButton
from src.Keyboard.Keyboard import Keyboard
from src.MethodsApi.MessageApi import MessageApi
from src.Objects.Message import Message_new
from src.Vk_Bot import VK_Bot
from src.BotEventGroup import BotEventGroup
from src.Vk_base import Vk_base


accessKeyGroup = "access_tokenGroup"
accessKeyUser = "access_tokenUser"
idGroup = "1234566"

"""
Создание клавиатуры с кнопками
"""
if __name__ == '__main__':
    def createKeyboardMain():
        keyboard = Keyboard()
        btnQuestion = TextButton(
            label="Задать вопрос", payload="question")
        btnPrice = OpenLinkButton(
            label="Узнать цену", payload="price", link="https://dev.vk.com/method/messages")
        btnBook = TextButton(label="Забронировать", payload="book")
        #Добавляет кнопки на одной линии
        keyboard.addButton([btnQuestion, btnPrice])
        #Добавляет кнопку занимающую всю ширину
        keyboard.addButton([btnBook])
        return keyboard.getKeyboard()

    async def main():
        async with aiohttp.ClientSession() as session:
            bot = VK_Bot(accessKeyGroup=accessKeyGroup,
                         session=session, idGroup=idGroup)
            VK = Vk_base(accessKeyGroup=accessKeyGroup,
                         accessKeyUser=accessKeyUser, session=session)
            MessageApi.vk = VK
            async for data in bot.listen():
                if data[0] == BotEventGroup.MESSAGE_NEW:
                    message_new: Message_new = Message_new(data[1])
                    if message_new.payload:
                        typeButton: dict = HandlerJson.json_to_dict(message_new.payload)
                        #Отслеживание нажатие кнопки начать
                        if typeButton.get("command", "") == "start":
                            message_new = Message_new(data[1])
                            params = {
                                "user_id": message_new.from_id,
                                "peer_id": message_new.from_id,
                                "message": "Добрый день",
                                "keyboard": createKeyboardMain(),
                            }
                            await MessageApi.send(params=params)
                        # Обработка нажатия на кнопку
                        if typeButton.get("button", "") == "question":
                            params = {
                                "user_id": message_new.from_id,
                                "peer_id": message_new.peer_id,
                                "message": "Какой у вас вопрос?",
                            }
                            await MessageApi.send(params=params)
                    if message_new.text == "Help":
                        params = {
                            "user_id": message_new.from_id,
                            "peer_id": message_new.from_id,
                            "message": "Чем помочь?",
                            "keyboard": createKeyboardMain(),
                        }
                        await MessageApi.send(params=params)
    asyncio.run(main())
