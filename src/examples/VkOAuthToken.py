import asyncio
import aiohttp
from src.Permisions import PermissionsGroup, PermissionsUser

from src.Vk_OAuth import Vk_OAuth

idGroup = "12345678"  # id группы
clientId = "147788"  # id приложения

"""
    Для получения token вызывается метод generateAccessLinkGroup или generateAccessLinkUser,
    для группы и пользователя соотвественно, после чего откроется новое окно в браузере,
    где нужно разрешить доступ и скопировать заначение access_token из ссылки в новом окне,
    токен необходим для работы с методами API.
    Подробнее https://dev.vk.com/api/access-token/implicit-flow-community, 
              https://dev.vk.com/api/access-token/implicit-flow-user
"""
if __name__ == '__main__':
    async def main():
        async with aiohttp.ClientSession() as session:
            oAuth = Vk_OAuth(session)
            ##Для получения Access token группы
            scope = PermissionsGroup.MESSAGES | PermissionsGroup.PHOTOS
            oAuth.generateAccessLinkGroup(clientId=clientId, group_id=idGroup, scope=scope)
            ##Для получения Access token пользователя
            scope = PermissionsUser.MESSAGES | PermissionsUser.PHOTOS | PermissionsUser.WALL
            oAuth.generateAccessLinkUser(clientId=clientId, scope=scope)
    asyncio.run(main())
