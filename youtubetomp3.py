import ssl
from moviepy.editor import *
from pytube import YouTube
from pytube import Playlist
from pathlib import Path

ssl._create_default_https_context = ssl._create_unverified_context


def youtube_to_mp4(url: str) -> str:
    vid = YouTube(url)
    video = vid.streams.filter().first()
    filepath = video.download(output_path=r'/Users/tyrone/Documents/Music/Videos')
    return filepath


def mp4_to_mp3(mp4_file: str):
    video = VideoFileClip(mp4_file)
    file_path = Path('/Users/tyrone/Documents/Music') / (Path(mp4_file).stem + ".mp3")
    audio = video.audio.write_audiofile(file_path)
    return audio


def youtube_to_mp3(url):
    song_name = YouTube(url).title
    video_path = youtube_to_mp4(url)
    mp3_path = mp4_to_mp3(video_path)

    print(f'Song: {song_name} successfully downloaded!')

    return mp3_path, song_name


def playlist_downloader(link):
    url = Playlist(link)
    print(f'Downloading: {url.title}')
    for video in url.videos:
        video.streams.first().download(output_path=r'/Users/tyrone/Documents/Music/Videos')
