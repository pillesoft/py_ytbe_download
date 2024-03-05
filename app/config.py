
class Config(object):
    FFMPEG_PATH=None
    DOWNLOADED_PATH='downloaded'

class DevelopmentConfig(Config):
    FFMPEG_PATH='ffmpeg-2024-02-04-git-7375a6ca7b-full_build\\bin\\ffmpeg.exe'

class ProductionConfig(Config):
    DOWNLOADED_PATH='/var/YTD/Downloaded'
