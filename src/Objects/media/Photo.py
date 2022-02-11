from enum import Enum
from typing import List


class Photo:
    """
        Объект, описывающий фотографию
        Побробнее https://dev.vk.com/reference/objects/photo
    """

    def __init__(self, item: dict) -> None:
        self.id: int = item.get("id", 0)
        self.album_id: int = item.get("album_id", 0)
        self.owner_id: int = item.get("owner_id", 0)
        self.user_id: int = item.get("user_id", 0)
        self.date: int = item.get("random_id", 0)
        self.text: str = item.get("text", "")
        self.sizes: List[Sizes] = self.getSizes(item.get("sizes", []))
        self.width: int = item.get("random_id", 0)
        self.height: int = item.get("random_id", 0)

    def getSizes(self, json):
        sizes: List[Sizes] = []
        for size in json:
            sizes.append(Sizes(size))
        return sizes

    def getOriginal(self):
        for size in self.sizes:
            if size.type == TypePhotoSize.Z:
                return size 
        return None



class Sizes:
    """
        Объект, описывающий изображения в разных размерах
        Побробнее https://dev.vk.com/reference/objects/photo-sizes
    """

    def __init__(self, item: dict) -> None:
        self.url: str = item.get("url", "")
        self.width: int = item.get("width", 0)
        self.height: int = item.get("height", 0)
        self.type: TypePhotoSize = TypePhotoSize(item.get("type", ""))


class TypePhotoSize(Enum):
    S = "s"  # — Пропорциональная копия изображения с максимальной стороной 75px;
    M = "m"  # — Пропорциональная копия изображения с максимальной стороной 130px;
    X = "x"  # — Пропорциональная копия изображения с максимальной стороной 604px;
    O = "o"  # — Если соотношение "ширина/высота" исходного изображения меньше или равно 3:2, то пропорциональная копия с максимальной стороной 130px. Если соотношение "ширина/высота" больше 3:2, то копия обрезанного слева изображения с максимальной стороной 130px и соотношением сторон 3:2.
    P = "p"  # — Если соотношение "ширина/высота" исходного изображения меньше или равно 3:2, то пропорциональная копия с максимальной стороной 200px. Если соотношение "ширина/высота" больше 3:2, то копия обрезанного слева и справа изображения с максимальной стороной 200px и соотношением сторон 3:2.
    Q = "q"  # — Если соотношение "ширина/высота" исходного изображения меньше или равно 3:2, то пропорциональная копия с максимальной стороной 320px. Если соотношение "ширина/высота" больше 3:2, то копия обрезанного слева и справа изображения с максимальной стороной 320px и соотношением сторон 3:2.
    R = "r"  # — Если соотношение "ширина/высота" исходного изображения меньше или равно 3:2, то пропорциональная копия с максимальной стороной 510px. Если соотношение "ширина/высота" больше 3:2, то копия обрезанного слева и справа изображения с максимальной стороной 510px и соотношением сторон 3:2
    Y = "y"  # — Пропорциональная копия изображения с максимальной стороной 807px;
    Z = "z"  # — Пропорциональная копия изображения с максимальным размером 1080x1024;
    W = "w"  # — Пропорциональная копия изображения с максимальным размером 2560x2048px.
    XZ = ""
