import isodate
import datetime

from src.channel import Channel


class PlayList:
    """
    класс для информации о плейлисте по его ID
    """

    def __init__(self, playlist_id: str) -> None:
        """Экземпляр инициализируется id плейлиста.
        __playlist --- вся информация о плейлисте
        id --- id плейлиста
        title --- название плейлиста
        description ---- описание плейлиста
        url --- ссылка на плейлист
        video_count --- количество видео
        """
        self.__playlist = Channel.get_service().playlists().list(id=playlist_id,
                                                                 part='contentDetails,snippet',
                                                                 maxResults=50,
                                                                 ).execute()
        self.__id = playlist_id
        self.__title = self.__playlist["items"][0]["snippet"]["title"]
        self.__description = self.__playlist["items"][0]["snippet"]["description"]
        self.__url = f'https://www.youtube.com/playlist?list={playlist_id}'
        self.__video_count = int(self.__playlist["items"][0]["contentDetails"]["itemCount"])
        self.__playlist_videos = Channel.get_service().playlistItems().list(playlistId=playlist_id,
                                                                            part='contentDetails',
                                                                            maxResults=50,
                                                                            ).execute()
        self.__video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__playlist_videos['items']]
        self.__video_response = Channel.get_service().videos().list(part='contentDetails,statistics',
                                                                    id=','.join(self.__video_ids)
                                                                    ).execute()

    @property
    def total_duration(self):
        all_duration = datetime.timedelta(0)
        for video in self.__video_response['items']:
            # YouTube video duration is in ISO 8601 format
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            all_duration += duration
            # print(duration)

        return all_duration

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__id})'

    def __str__(self):
        return self.__title

    @property
    def playlist(self):
        return self.__playlist

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def url(self):
        return self.__url

    @property
    def description(self):
        return self.__description

    @property
    def video_count(self):
        return self.__video_count

    @property
    def playlist_videos(self):
        return self.__playlist_videos

    def show_best_video(self):
        link = ''
        max_likes = 0
        for video in self.__video_response['items']:
            current_likes = int(video["statistics"]["likeCount"])
            if current_likes > max_likes:
                max_likes = current_likes
                link = f'https://youtu.be/{video["id"]}'

        return link
