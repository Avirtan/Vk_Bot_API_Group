from typing import List
from src.Keyboard.Button import Button
import json


class Keyboard:
    """
    Класс для создание клавиатуры из кнопок
    Подробнее https://dev.vk.com/api/bots/development/keyboard
    """
    def __init__(self, one_time: bool = False, inline:bool=False) -> None:
        self.data: dict = {
            "one_time": False,
            "inline": False,
            "buttons": []
        }
        self.buttons: list = []
        self.data["one_time"] = one_time
        self.data["inline"] = inline

    def addButton(self, buttons: List[Button]):
        tmpArray: list = []
        for button in buttons:
            tmpArray.append(button.getAction())
        self.buttons.append(tmpArray)
        self.data["buttons"] = self.buttons

    def getKeyboard(self):
        return json.dumps(self.data)
