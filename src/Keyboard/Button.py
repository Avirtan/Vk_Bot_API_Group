from src.Keyboard.Color import Color
from enum import Enum


class Button:
    """
    Класса на создание кнопок для клавиатуры
    Подробнее https://dev.vk.com/api/bots/development/keyboard
    """
    def __init__(self, label: str, payload: str) -> None:
        self.__action = {
            "action": {},
        }
        self.__action["action"]["label"] = label
        self.__action["action"]["payload"] = "{\"button\":  \"%s\" }" % payload

    def getAction(self):
        return self.__action

class TextButton(Button):
    """
    Текстовая кнопка
    Отправляет сообщение c текстом, указанным в label
    """
    def __init__(self, label: str, payload: str, color: Color = Color.PRIMARY) -> None:
        super().__init__(label, payload)
        self.__action = super().getAction()
        self.__action["action"]["type"] = TypeButton.TEXT.value
        self.__action["color"] = color.value

class OpenLinkButton(Button):
    """
    Текстовая кнопка
    Отправляет сообщение c текстом, указанным в label
    """
    def __init__(self, label: str, payload: str, link:str) -> None:
        super().__init__(label, payload)
        self.__action = super().getAction()
        self.__action["action"]["type"] = TypeButton.OPEN_LINK.value
        self.__action["action"]["link"] = link

class TypeButton(Enum):
    TEXT = "text"
    OPEN_LINK = "open_link"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    CALLBACK = "callback"
