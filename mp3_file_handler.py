import eyed3
import requests
from eyed3 import AudioFile
from pytube import YouTube
from pytube import Playlist
from pathlib import Path
from moviepy.video.io.VideoFileClip import VideoFileClip


class MusicHandler:
    """
    Class that handles downloading videos from YouTube and editing their metadata so that they're formatted properly
    for Spotify.
    """

    def __init__(self):
        self.video_output_path = Path(r'/Users/tyronedike/Documents/Music/Videos')
        self.mp3_output_path = Path('/Users/tyronedike/Documents/Music')

    def youtube_to_mp4(self, url: str) -> str:
        """
        Converts YouTube videos to MP4
        :param url: YouTube video to download.
        :return: File path of downloaded song.
        """
        vid = YouTube(url)
        video = vid.streams.filter().first()
        filepath = video.download(output_path=self.video_output_path)
        return filepath

    def youtube_to_mp3(self, url) -> str:
        """
        Utilizes the youtube_to_mp4 and mp4_to_mp3 functions to automate the process, done to handle error that was
        present with downloading from YouTube to MP3 directly.

        :param url: YouTube video to download
        :return: Path of mp3 file.
        """
        song_name = YouTube(url).title
        video_path = self.youtube_to_mp4(url)
        mp3_path = self.mp4_to_mp3(video_path)
        print(f'Song: {song_name} successfully downloaded!')

        return mp3_path

    def mp4_to_mp3(self, mp4_file: str) -> str:
        """

        :param mp4_file: MP4 files to download
        :return: audio of the mp4 file.
        """
        video = VideoFileClip(mp4_file)
        file_path = self.mp3_output_path / (Path(mp4_file).stem + ".mp3")
        audio = video.audio.write_audiofile(file_path)
        return audio

    def playlist_downloader(self, link) -> None:
        """
        Downloads multiple files from YouTube at once using Playlist class.
        :param link: Link to playlist.
        :return: None
        """
        url = Playlist(link)
        print(f'Downloading: {url.title}')
        for video in url.videos:
            video.streams.first().download(output_path=str(self.video_output_path))

    def playlist_to_mp3(self) -> None:
        """
        Bulk Converts Albums in video file path to mp3.
        :return: None
        """
        for file in self.video_output_path.iterdir():
            if file.suffix.endswith('.mp4'):
                self.mp4_to_mp3(str(file))

    @staticmethod
    def meta_data(path: str, parameters: dict) -> None:
        """

        :param path: File that I want to edit the metadata of.
        :param parameters: Dictionary to handle the metadata.
        :return:
        """
        audio_file: AudioFile = eyed3.load(path)
        response = requests.get(parameters['Album Art'])

        if parameters['Title']:
            audio_file.tag.title = parameters['Title']
        if parameters.get('Artist'):
            audio_file.tag.artist = str(parameters['Artist'])
        if parameters['Album']:
            audio_file.tag.album = parameters['Album']
        if parameters['Track Number']:
            audio_file.tag.track_num = parameters['Track Number']
        if parameters['Album Art']:
            audio_file.tag.images.set(3, response.content, 'image/jpeg')

        audio_file.tag.save()

    @staticmethod
    def bulk_update_album_art(image_link: str) -> None:
        """
        Updates album art using requests library by allowing users to select a photo from the web which is then applied
        to the mp3 files.
        :param image_link: Image that you want to use.
        :return: None
        """
        path = input('Enter a File Path: ')
        for mp3_file in Path(path).iterdir():
            if mp3_file.suffix == '.mp3':
                response = requests.get(image_link)
                audio_file = eyed3.load(mp3_file)
                audio_file.tag.images.set(3, response.content, 'image/jpeg')
                audio_file.tag.save()


app = MusicHandler()

app.youtube_to_mp3('https://www.youtube.com/watch?v=8caDDy8mNmM')
