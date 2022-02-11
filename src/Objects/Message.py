from array import array
from typing import Any


class Message:
    """
        Объект типа Личное сообщение
        Побробнее https://dev.vk.com/reference/objects/message
    """
    def __init__(self, list: dict, new:bool=True) -> None:
        message: dict = list["object"]["message"]
        if not new:
            message = list["object"]
        self.id: int = message.get("id", 0)
        self.date: int = message.get("date", 0)
        self.peer_id: int = message.get("peer_id", 0)
        self.from_id: int = message.get("from_id", 0)
        self.text: str = message.get("text", "") 
        self.random_id: int = message.get("random_id", 0)
        self.ref: str = message.get("ref", "")
        self.ref_source: str = message.get("ref_source", "")
        self.attachments: array = message.get("attachments", [])
        self.important: bool = message.get("important", False)
        self.geo: any = message.get("geo", None)
        self.payload: str = message.get("payload", "")
        self.keyboard: str = message.get("keyboard", "")
        self.fwd_messages: array = message.get("fwd_messages")
        self.reply_message: any = message.get("reply_message", None)
        self.action: any = message.get("action", None)
        self.admin_author_id: int = message.get("admin_author_id", 0)
        self.conversation_message_id: int = message.get(
            "conversation_message_id", 0)
        self.is_cropped: bool = message.get("is_cropped", False)
        self.members_count:int = message.get("members_count", 0)
        self.update_time:int = message.get("update_time", 0)
        self.was_listened:bool = message.get("was_listened", bool)
        self.pinned_at:bool = message.get("pinned_at", False)
        self.message_tag:str = message.get("message_tag", "")

    def __str__(self) -> str:
        return f"message {self.text} from user {self.from_id}"


class Message_new(Message):
    """
    Класс для сериализации данных при при 
    Event message_new
    """
    def __init__(self, list: dict) -> None:
        super().__init__(list)

    def __str__(self) -> str:
        return f"message {self.text} from user {self.from_id}"

class Message_reply_edit(Message):
    """
    Класс для сериализации данных при при 
    Event message_reply или message_edit
    """
    def __init__(self, list: dict) -> None:
        super().__init__(list, new=False)

    def __str__(self) -> str:
        return f"message {self.text} from user {self.from_id}"


class Message_typing:
    """
     Класс для сериализации данных при при 
    Event message_typing_state
    """
    def __init__(self, list: dict) -> None:
        message: dict = list["object"]
        self.from_id:int = message.get("from_id", 0)
        self.to_id:int = message.get("to_id", 0)
    
    def __str__(self) -> str:
        return f"from {self.from_id} to  {self.to_id}"

class Message_allow:
    """
    Класс для сериализации данных при при 
    Event message_allow
    """
    def __init__(self, list: dict) -> None:
        message: dict = list["object"]
        self.user_id:int = message.get("user_id", "")
        self.key:str = message.get("key", "")
    
    def __str__(self) -> str:
        return f"from {self.user_id} to  {self.key}"

class Message_deny:
    """
    Класс для сериализации данных при при 
    Event message_deny
    """
    def __init__(self, list: dict) -> None:
        message: dict = list["object"]
        self.user_id:int = message.get("user_id", "")
    
    def __str__(self) -> str:
        return f"from {self.user_id}"

class Message_event:
    """
    Используется для работы с Callback-кнопками
    Класс для сериализации данных при при 
    Event message_event
    """
    def __init__(self, list: dict) -> None:
        message: dict = list["object"]
        self.user_id:int = message.get("user_id", "")
        self.peer_id:int = message.get("peer_id", "")
        self.event_id:int = message.get("event_id", "")
        self.payload:str = message.get("payload", "")
        self.conversation_message_id:int = message.get("conversation_message_id", "")        
    
    def __str__(self) -> str:
        return f"from {self.user_id}"

