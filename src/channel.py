import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key = os.environ.get('API_KEY')

# создать специальный объект для работы с API
# youtube = build('youtube', 'v3', developerKey=api_key)
# поскольку у меня теперь есть Channel.get_service(), то я могу создавать эту специальную переменную сразу внутри класса



class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API.
        Имеет следующие поля
        channel --- вся информаци
        id --- id канала
        title --- название канала
        description ---- описание канала
        url --- ссылка на канал
        subscriber_count --- количество подписчиков
        video_count --- количество видео
        views_count --- общее количество просмотров"""
        # self.__channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel = Channel.get_service().channels().list(id=channel_id, part='snippet,statistics').execute()
        self.__channel_id = self.__channel["items"][0]["id"]
        self.__title = self.__channel["items"][0]["snippet"]["title"]
        self.__description = self.__channel["items"][0]["snippet"]["description"]
        self.__url = "https://www.youtube.com/" + self.__channel["items"][0]["snippet"]["customUrl"] if \
            self.__channel["items"][0]["snippet"]["customUrl"] \
            else "https://www.youtube.com/channel/" + self.__channel_id
        self.__subscriber_count = int(self.__channel['items'][0]['statistics']['subscriberCount'])
        self.__video_count = int(self.__channel['items'][0]['statistics']['videoCount'])
        self.__views_count = int(self.__channel['items'][0]['statistics']['viewCount'])

    def __str__(self):
        return f"{self.__title} ({self.__url})"
        # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'

    def __add__(self, other):
        return self.__subscriber_count + other.__subscriber_count

    def __sub__(self, other):
        return self.__subscriber_count - other.__subscriber_count

    def __lt__(self, other):
        return self.__subscriber_count < other.__subscriber_count

    def __le__(self, other):
        return self.__subscriber_count <= other.__subscriber_count

    def __gt__(self, other):
        return self.__subscriber_count > other.__subscriber_count

    def __ge__(self, other):
        return self.__subscriber_count >= other.__subscriber_count

    def __eq__(self, other):
        return self.__subscriber_count == other.__subscriber_count

    @property
    def channel(self):
        return self.__channel

    @property
    def channel_id(self):
        return self.__channel_id

    @property
    def title(self):
        return self.__title

    @property
    def description(self):
        return self.__description

    @property
    def url(self):
        return self.__url

    @property
    def subscriber_count(self):
        return self.__subscriber_count

    @property
    def video_count(self):
        return self.__video_count

    @property
    def views_count(self):
        return self.__views_count

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        Channel.printj(self.__channel)

    @classmethod
    def get_service(cls):
        return build('youtube', 'v3', developerKey=api_key)

    def to_json(self, filename):
        atributes = {
                        # "channel": self.__channel,
                        "channel_id": self.__channel_id,
                        "title": self.__title,
                        "description": self.__description,
                        "url": self.__url,
                        "subscriber_count": self.__subscriber_count,
                        "video_count": self.__video_count,
                        "views_count": self.__views_count
        }
        with open(filename, 'w') as file:
            json.dump(atributes, file)
            # file.write(json.dumps(atributes))

# moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
# moscowpython.print_info()
#
# print('')
# print(moscowpython.id)
# print(moscowpython.url)
# print(moscowpython.subscriber_count)
# print(moscowpython.video_count)
# print(moscowpython.views_count)
# print('')
# print(moscowpython.channel["items"][0]["snippet"]["customUrl"])

# youtube = Channel.get_service()

# channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
# channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
# Channel.printj(channel)


# moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
# highload = Channel('UCwHL6WHUarjGfUM_586me8w')
#
# # Используем различные магические методы
# print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
# print(moscowpython + highload)  # 100100
# print(moscowpython - highload)  # -48300
# print(highload - moscowpython)  # 48300
# print(moscowpython > highload)  # False
# print(moscowpython >= highload)  # False
# print(moscowpython < highload)  # True
# print(moscowpython <= highload)  # True
# print(moscowpython == highload)  # False
