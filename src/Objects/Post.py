import array
from typing import List

from src.Objects.media.Photo import Photo

class Post:
    """
        Объект, описывающий запись на стене пользователя или сообщества
        Побробнее https://dev.vk.com/reference/objects/post
    """
    def __init__(self, item: dict) -> None:
        self.id: int = item.get("id", 0)
        self.owner_id: int = item.get("owner_id", 0)
        self.from_id: int = item.get("from_id", 0)
        self.created_by: int = item.get("created_by", 0) 
        self.date: int = item.get("random_id", 0)
        self.text: str = item.get("text", "")
        self.reply_owner_id: int = item.get("reply_owner_id", "")
        self.reply_post_id: int = item.get("reply_post_id", "")
        self.friends_only: int = item.get("friends_only", "")
        self.comments: any = item.get("comments", None)
        self.copyright: any = item.get("copyright", None)
        self.likes: any = item.get("likes", None)
        self.reposts: any = item.get("reposts", None)
        self.views: any = item.get("views", None)
        self.post_type: str = item.get("post_type", None)
        self.post_source: any = item.get("post_source", None)
        self.attachments: array = item.get("attachments", [])
        self.geo: any = item.get("geo", None)
        self.signer_id:int = item.get("signer_id", 0)
        self.copy_history: array = item.get("copy_history", [])
        self.can_pin:int = item.get("can_pin", 0)
        self.can_delete:int = item.get("can_delete", 0)
        self.can_edit:int = item.get("can_edit", 0)
        self.is_pinned:int = item.get("is_pinned", 0)
        self.marked_as_ads:int = item.get("marked_as_ads", 0)
        self.is_favorite:bool = item.get("is_favorite", 0)
        self.donut: any = item.get("donut", None)
        self.postponed_id:int = item.get("postponed_id", 0)
    
    @staticmethod
    def json_to_posts(json:List):
        posts:List[Post] = []
        for post in json["response"]["items"]:
            posts.append(Post(post))
        return posts 

    def getPhotos(self):
        photos:List[Photo] = []
        for photo in self.attachments:
            if photo["type"] == "photo":
                tmpPhoto = Photo(photo["photo"])
                photos.append(tmpPhoto)
        return photos



