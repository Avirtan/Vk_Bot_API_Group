from enum import Enum


class BotEventGroup(Enum):
    """
        Основные события в сообществах 
        Подробнее https://dev.vk.com/api/community-events/json-schema
    """
    # Сообщения ###################################
    MESSAGE_NEW = "message_new"  # входящее сообщение.
    MESSAGE_REPLY = "message_reply"  # новое исходящее сообщение
    MESSAGE_EDIT = "message_edit"  # редактирование сообщения
    MESSAGE_ALLOW = "message_allow"  # подписка на сообщения от сообщества
    MESSAGE_DENY = "message_deny"  # новый запрет сообщений от сообщества
    MESSAGE_TYPING = "message_typing_state"  # статус набора текста
    MESSAGE_EVENT = "message_event"  # действие с сообщением. Используется для работы с Callback-кнопками
    #Фотографии ###################################
    PHOTO_NEW = "photo_new"  # добавление фотографии
    PHOTO_COMMENT_NEW = "photo_comment_new"  # добавление комментария к фотографии
    # редактирование комментария к фотографии
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    # восстановление комментария к фотографии
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    # Аудиозаписи #############################################
    AUTIO_NEW = "audio_new"  # добавление аудио
    # Видеозаписи ##################################
    VIDEO_NEW = "video_new"  # добавление видео
    VIDEO_COMMENT_NEW = "video_comment_new"  # комментарий к видео
    VIDEO_COMMENT_EDIT = "video_comment_edit"  # комментарий к видео
    # редактирование комментария к видео
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    # восстановление комментария к видео
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    # Записи на стене ##############################
    WALL_POST_NEW = "wall_post_new"  # запись на стене
    WALL_REPOST = "wall_repost"  # репост записи из сообщества
    WALL_REPLY_NEW = "wall_reply_new"  # добавление комментария на стене
    WALL_REPLY_EDIT = "wall_reply_edit"  # редактирование комментария на стене
    WALL_REPLY_RESTORE = "wall_reply_restore"  # восстановление комментария на стене
    WALL_REPLY_DELETE = "wall_reply_delete"  # удаление комментария на стене
    # Мне нравится ##################################
    LIKE_ADD = "like_add"  # событие о новой отметке Мне нравится
    LIKE_REMOVE = "like_remove"  # событие о снятии отметки Мне нравится
    # Обсуждения #####################################
    BOARD_POST_NEW = "board_post_new"  # создание комментария в обсуждении
    BOARD_POST_EDIT = "board_post_edit"  # редактирование комментария
    BOARD_POST_RESTORE = "board_post_restore"  # восстановление комментария
    BOARD_POST_DELETE = "board_post_delete"  # удаление комментария в обсуждении
    # Товары #########################################
    MARKET_COMMENT_NEW = "market_comment_new"  #новый комментарий к товару
    MARKET_COMMENT_EDIT = "market_comment_edit"  #редактирование комментария к товару
    MARKET_COMMENT_RESTORE = "market_comment_restore" # восстановление комментария к товару
    MARKET_COMMENT_DELETE = "market_comment_delete"  # удаление комментария к товару
    MARKET_ORDER_NEW = "market_order_new"  # новый заказ
    MARKET_ORDER_EDIT = "market_order_edit"  # редактирование заказа
    # Пользователи ##############################################
    GROUP_LEAVE = "group_leave" #удаление участника из сообщества
    GROUP_JOIN = "group_join" #добавление участника или заявки на вступление в сообщество
    USER_BLOCK = "user_block" #добавление пользователя в чёрный список
    USER_UNBLOCK = "user_unblock" #удаление пользователя из чёрного списка
    # Прочее ################################################
    POLL_VOTE_NEW = "poll_vote_new" #добавление голоса в публичном опросе
    GROUP_OFFICERS_EDIT = "group_officers_edit" #редактирование списка руководителей
    GROUP_CHANGE_SETTINGS = "group_change_settings" #изменение настроек сообщества
    GROUP_CHANGE_PHOTO = "group_change_photo" #изменение главного фото
    VKPAY_TRANSACTION = "vkpay_transaction" #платёж через VK Pay
    APP_PAYLOAD = "app_payload" #событие в VK Mini Apps
    DONUT_SUBSCRIPTION_CREATE = "donut_subscription_create" #создание подписки VK Donut
    DONUT_SUBSCRIPTION_PROLONGED = "donut_subscription_prolonged" #продление подписки
    DONUT_SUBSCRIPTION_EXPIRED = "donut_subscription_expired" #подписка истекла
    DONUT_SUBSCRIPTION_CANCELLED = "donut_subscription_cancelled" #отмена подписки
    DONUT_SUBSCRIPTION_PRICE_CHANGED = "donut_subscription_price_changed" #изменение стоимости подписки
    DONUT_MONEY_WITHDRAW = "donut_money_withdraw" #вывод денег
    DONUT_MONEY_WITHDRAW_ERROR = "donut_money_withdraw_error" #ошибка вывода денег
    ##################################
    EVENT_EMPTY = ""
    EVENT_ERROR = ""