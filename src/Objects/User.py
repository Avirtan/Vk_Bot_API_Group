import array


class User:
    """
        Объект содержит информацию о пользователе ВКонтакте
        Побробнее https://dev.vk.com/reference/objects/user
    """
    def __init__(self, item: dict) -> None:
        self.id: int = item.get("id", 0)
        self.first_name: str = item.get("first_name", "")
        self.last_name: str = item.get("last_name", '')
        self.deactivated: bool = item.get("deactivated", False)
        self.is_closed: bool = item.get("is_closed", False)
        self.can_access_closed: bool = item.get("can_access_closed", False)
        ##Опциональные поля
        self.about: str = item.get("about", "")
        self.activities: str = item.get("activities", "")
        self.bdate: str = item.get("bdate", "")
        self.blacklisted: int = item.get("blacklisted", 0)
        self.blacklisted_by_me: int = item.get("blacklisted_by_me", 0)
        self.books: str = item.get("books", "")
        self.can_post: int = item.get("can_post", 0)
        self.can_see_all_posts: int = item.get("can_see_all_posts", 0)
        self.can_see_audio: int = item.get("can_see_audio", 0)
        self.can_send_friend_request: int = item.get("can_send_friend_request", 0)
        self.can_write_private_message: int = item.get("can_write_private_message", 0)
        self.career: any = item.get("career", None) ##TODO 
        self.city: any = item.get("city", None) ##TODO 
        self.common_count: int = item.get("common_count", 0)
        self.connections: any = item.get("connections", None) ##TODO 
        self.contacts: any = item.get("contacts", None) ##TODO 
        self.counters: any = item.get("counters", None) ##TODO 
        self.country: any = item.get("country", None) ##TODO 
        self.crop_photo: any = item.get("crop_photo", None) ##TODO 
        self.domain: str = item.get("domain", "")
        self.education: any = item.get("education", None) ##TODO 
        self.exports: any = item.get("exports", None) ##TODO 
        self.first_name_nom: str = item.get("first_name_nom", "")
        self.followers_count: int = item.get("followers_count", 0)
        self.friend_status: int = item.get("friend_status", 0)
        self.games: str = item.get("games", "")
        self.has_mobile: int = item.get("has_mobile", 0)
        self.has_photo: int = item.get("has_photo", 0)
        self.home_town: str = item.get("home_town", "")
        self.interests: str = item.get("interests", "")
        self.is_favorite: int = item.get("is_favorite", 0)
        self.is_friend: int = item.get("is_friend", 0)
        self.is_hidden_from_feed: int = item.get("is_hidden_from_feed", 0)
        self.is_no_index: int = item.get("is_no_index", 0)
        self.last_name_nom: str = item.get("last_name_nom", "")
        self.last_seen: any = item.get("last_seen", None) ##TODO 
        self.lists: str = item.get("lists", "")
        self.maiden_name: str = item.get("maiden_name", "")
        self.military: any = item.get("military", None) ##TODO 
        self.movies: str = item.get("movies", "")
        self.music: str = item.get("music", "")
        self.nickname: str = item.get("nickname", "")
        self.occupation: any = item.get("occupation", None) ##TODO 
        self.online: int = item.get("online", 0)
        self.personal: any = item.get("personal", None) ##TODO 
        self.photo_50: str = item.get("photo_50", "")
        self.photo_100: str = item.get("photo_100", "")
        self.photo_200_orig: str = item.get("photo_200_orig", "")
        self.photo_200: str = item.get("photo_200", "")
        self.photo_400_orig: str = item.get("photo_400_orig", "")
        self.photo_id: str = item.get("photo_id", "")
        self.photo_max: str = item.get("photo_max", "")
        self.photo_max_orig: str = item.get("photo_max_orig", "")
        self.quotes: str = item.get("quotes", "")
        self.relatives: array = item.get("relatives", []) ##TODO 
        self.relation: int = item.get("relation", 0)
        self.schools: array = item.get("schools", []) ##TODO 
        self.screen_name: str = item.get("screen_name", "")
        self.sex: int = item.get("sex", 0)
        self.site: str = item.get("site", "")
        self.status: str = item.get("status", "")
        self.timezone: int = item.get("timezone", 0)
        self.trending: int = item.get("trending", 0)
        self.string: str = item.get("string", "")
        self.universities: array = item.get("universities", []) ##TODO 
        self.verified: int = item.get("verified", 0)
        self.wall_default: str = item.get("wall_default", "")