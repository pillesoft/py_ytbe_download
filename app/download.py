
# test command to download a video format
# yt-dlp -x -f best https://youtu.be/s_Zf49xYLmQ

# yt-dlp -x -f bestaudio --audio-format mp3 https://youtu.be/lhXFIz0pVv4 --ffmpeg-location ffmpeg-2024-02-04-git-7375a6ca7b-full_build\bin\ffmpeg.exe
# yt-dlp -x -f bestaudio https://youtu.be/lhXFIz0pVv4

# https://www.youtube.com/watch?v=QM1YnxbdTjg
# https://www.youtube.com/watch?v=jPCJIB1f7jk

# https://youtu.be/lhXFIz0pVv4
# https://www.youtube.com/watch?v=QM1YnxbdTjg
# https://www.youtube.com/watch?v=jPCJIB1f7jk
# https://youtu.be/s_Zf49xYLmQ

import yt_dlp
import os
from .mediafile import MediaFile


class Download:

    __mp3opts = {
        'proxy': '',
        'format': 'bestaudio/best',
        'outtmpl': 'var/downloaded/%(autonumber)s-%(title)s',
        'verbose': '',
        'ffmpeg_location': 'ffmpeg-2024-02-04-git-7375a6ca7b-full_build\\bin\\ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
        # 'logger': MyLogger(),
        # 'progress_hooks': [self.monitor],
    }

    __mp4opts = {
        'proxy': '',
        'format': 'best',
        'outtmpl': 'var/downloaded/%(autonumber)s-%(title)s.mp4',
        'verbose': '',
        'ffmpeg_location': 'ffmpeg-2024-02-04-git-7375a6ca7b-full_build\\bin\\ffmpeg.exe',
        # 'postprocessors': [{
        #     'key': 'FFmpegVideoConvertor',
        #     'preferredcodec': 'mp4',
            # 'ext': 'mp4'
        # }],
        # 'logger': MyLogger(),
        # 'progress_hooks': [monitor],
    }

    _files: list[MediaFile]

    @property
    def Files(self):
        return self._files
    
    def __init__(self):
        self._files = []

    def download_mp3(self, urls: list[str]):
        self.__mp3opts['progress_hooks'] = [self.monitor]

        with yt_dlp.YoutubeDL(self.__mp3opts) as ydl:
            for url in urls:
                file: MediaFile = MediaFile(url)
                self._files.append(file)
                try:
                    error_code = ydl.download(url)

                    file.Ext = '.mp3'
                    file.ErrorCode = error_code
                except yt_dlp.DownloadError as e:
                    file.ErrorDescription = e.msg

                # if error_code != 0:
                #     raise ConvertError(error_code)
        

    def download_mp4(self, url: list[str]):
        self.__mp4opts['progress_hooks'] = [self.monitor]

        with yt_dlp.YoutubeDL(self.__mp4opts) as ydl:
            error_code = ydl.download(url)
        if error_code != 0:
            raise ConvertError(error_code)
        
    def getFile(self, url: str):
        return [f for f in self._files if f.Url == url]


    def monitor(self, d):
        # if d['status'] == 'downloading':
        #     print('currently processing: ' + d['filename'])
        if d['status'] == 'finished':
            head, tail = os.path.split(d['filename'])
            f = self.getFile(d['info_dict']['original_url'])[0]
            f.Head = head
            f.Tail = tail
            

class ConvertError(Exception):
    
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.error_code = args[0]

