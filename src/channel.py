import json
import os

# необходимо установить через: pip install google-api-python-client
from googleapiclient.discovery import build

import isodate

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')



# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)




class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """Выводит словарь в json-подобном удобном формате с отступами"""
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        Channel.printj(self.channel)


# moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
# moscowpython.print_info()


# channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
# channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
# printj(channel)