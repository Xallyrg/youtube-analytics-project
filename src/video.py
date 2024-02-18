import json
import os
from googleapiclient.discovery import build

from src.channel import Channel

api_key = os.environ.get('API_KEY')


# # достать по ID канала
# channel_id = 'UCwHL6WHUarjGfUM_586me8w'  # HighLoad Channel
# channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
# # Channel.printj(channel)

# # достать по ID плейлиста
# playlist_id = 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC'
# playlist_videos = youtube.playlistItems().list(playlistId=playlist_id, part='contentDetails', maxResults=50, ).execute()
# # Channel.printj(playlist_videos)


# # достать по ID видео
# video_id = 'AWX4JnAnjBE'
# video_response = Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',id=video_id).execute()
# Channel.printj(video_response)
# # video_title: str = video_response['items'][0]['snippet']['title']
# # view_count: int = video_response['items'][0]['statistics']['viewCount']
# # like_count: int = video_response['items'][0]['statistics']['likeCount']
# # comment_count: int = video_response['items'][0]['statistics']['commentCount']


class Video:
    """
    класс для информации о видео по его ID
    """
    def __init__(self, video_id: str) -> None:
        """Экземпляр инициализируется id видео.
        video --- вся информация
        video_id --- id видео
        video_title --- название видео
        description ---- описание видео
        url --- ссылка на видео
        view_count --- количество просмотров
        like_count --- количество лайков
        comment_count --- количество комментариев"""
        self.__video = Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',id=video_id).execute()
        self.__video_id = video_id
        self.__video_title = self.__video['items'][0]['snippet']['title']
        self.__description = self.__video['items'][0]['snippet']['description']
        self.__url = f'https://www.youtube.com/watch?v={self.__video_id}'
        self.__view_count = int(self.__video['items'][0]['statistics']['viewCount'])
        self.__like_count = int(self.__video['items'][0]['statistics']['likeCount'])
        self.__comment_count = int(self.__video['items'][0]['statistics']['commentCount'])

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__video_id})'

    def __str__(self):
        return self.__video_title

    @property
    def video(self):
        return self.__video

    @property
    def video_id(self):
        return self.__video_id

    @property
    def video_title(self):
        return self.__video_title

    @property
    def description(self):
        return self.__description

    @property
    def url(self):
        return self.__url

    @property
    def view_count(self):
        return self.__view_count

    @property
    def like_count(self):
        return self.__like_count

    @property
    def comment_count(self):
        return self.__comment_count



# video1 = Video('AWX4JnAnjBE')
# Channel.printj(video1.video)
# print(video1.video_title)
# print(video1.description)
# print(video1.url)
# print(repr(video1))
# print(str(video1))




class PLVideo(Video):
    """
    Класс для информации о видео и плейлисте
    """
    def __init__(self, video_id: str, playlist_id: str) -> None:
        """
        Экземпляр инициализируется id видео.
        video --- вся информация
        video_id --- id видео
        video_title --- название видео
        description ---- описание видео
        url --- ссылка на видео в плейлисте (переопределен)
        view_count --- количество просмотров
        like_count --- количество лайков
        comment_count --- количество комментариев
        playlist_id --- id плейлиста (добавлен)
        """
        super().__init__(video_id)
        # self.__video = Channel.get_service().videos().list(part='snippet,statistics,contentDetails,topicDetails',id=video_id).execute()
        # self.__video_id = video_id
        # self.__video_title = self.__video['items'][0]['snippet']['title']
        # self.__description = self.__video['items'][0]['snippet']['description']
        self.__playlist_id = playlist_id
        self.__url = f'https://www.youtube.com/watch?v={self.video_id}&list={self.__playlist_id}'
        # self.__view_count = int(self.__video['items'][0]['statistics']['viewCount'])
        # self.__like_count = int(self.__video['items'][0]['statistics']['likeCount'])
        # self.__comment_count = int(self.__video['items'][0]['statistics']['commentCount'])


    @property
    def playlist_id(self):
        return self.__playlist_id

    @property
    def url(self):
        return self.__url

    def __repr__(self):
        return f'{self.__class__.__name__}({self.video_id}, {self.__playlist_id})'


video2 = PLVideo('4fObz_qw9u4', 'PLv_zOGKKxVph_8g2Mqc3LMhj0M_BfasbC')
# Channel.printj(video2.video)
# print(video2.video_title)
# print(video2.description)
# print(video2.url)
# print(video2.playlist_id)
# print(repr(video2))
# print(str(video2))
