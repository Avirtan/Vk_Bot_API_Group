import array


class Grpu:
    """
        Объект содержит информацию о сообществе ВКонтакте
        Побробнее https://dev.vk.com/reference/objects/group
    """
    def __init__(self, item: dict) -> None:
        self.id: int = item.get("id", 0)
        self.name: str = item.get("name", "")
        self.screen_name: str = item.get("screen_name", '')
        self.is_closed: int = item.get("is_closeds", 0)
        self.deactivated: str = item.get("deactivated", '')
        self.is_admin: int = item.get("is_admin", 0)
        self.admin_level: int = item.get("admin_level", 0) ##TODO 
        self.is_member: int = item.get("is_member", 0)
        self.is_advertiser: int = item.get("is_advertiser", 0)
        self.invited_by: int = item.get("invited_by", 0)
        self.type: str = item.get("type", '') ##TODO 
        self.photo_50: str = item.get("photo_50", '')
        self.photo_100: str = item.get("photo_100", '') 
        self.photo_200: str = item.get("photo_200", '') 
        ## Опциональные поля
        self.activity: str = item.get("activity", '') 
        self.addresses: any = item.get("addresses", None) ##TODO 
        self.age_limits: int = item.get("age_limits", 0)
        self.ban_info: any = item.get("ban_info", None) ##TODO 
        self.can_create_topic: int = item.get("can_create_topic", 0)
        self.can_message: int = item.get("can_message", 0)
        self.can_post: int = item.get("can_post", 0)
        self.can_see_all_posts: int = item.get("can_see_all_posts", 0)
        self.can_upload_doc: int = item.get("can_upload_doc", 0)
        self.can_upload_video: int = item.get("can_upload_video", 0)
        self.city: any = item.get("city", None) ##TODO 
        self.contacts: array = item.get("contacts", []) ##TODO 
        self.counters: any = item.get("counters", None) ##TODO 
        self.country: any = item.get("country", None) ##TODO 
        self.cover: any = item.get("cover", None) ##TODO 
        self.crop_photo: any = item.get("crop_photo", None) ##TODO 
        self.description: str = item.get("descriptions", '') 
        self.fixed_post: int = item.get("fixed_post", 0)
        self.has_photo: int = item.get("has_photo", 0)
        self.is_favorite: int = item.get("is_favorite", 0)
        self.is_hidden_from_feed: int = item.get("is_hidden_from_feed", 0)
        self.is_messages_blocked: int = item.get("is_messages_blocked", 0)
        self.links: array = item.get("links", []) ##TODO 
        self.main_album_id: int = item.get("main_album_id", 0)
        self.main_section: int = item.get("main_section", 0)
        self.market: any = item.get("market", None) ##TODO 
        self.member_status: int = item.get("member_status", 0)
        self.members_count: int = item.get("members_count", 0)
        self.place: any = item.get("place", None) ##TODO 
        self.public_date_label: str = item.get("public_date_label", '') 
        self.site: str = item.get("site", '') 
        self.start_date: any = item.get("place", None) 
        self.finish_date: any = item.get("place", None) 
        self.status: str = item.get("status", '') 
        self.trending: int = item.get("trending", 0)
        self.verified: int = item.get("verified", 0)
        self.wall: int = item.get("wall", 0)
        self.wiki_page: str = item.get("wiki_page", '') 