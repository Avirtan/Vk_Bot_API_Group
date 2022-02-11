import aiohttp


class Vk_base:
    """
    Базовый класс для сохранения ключей и сессии, используется для работы с методами апи
    """
    accessKeyGroup: str = ""
    accessKeyUser: str = ""
    session:aiohttp.ClientSession = None
    versionApi = "5.131"
    
    def __init__(self, accessKeyGroup, accessKeyUser, session:aiohttp.ClientSession) -> None:
        self.accessKeyGroup = accessKeyGroup
        self.accessKeyUser = accessKeyUser
        self.session = session
