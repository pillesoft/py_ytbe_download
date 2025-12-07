
class Config(object):
    FFMPEG_PATH=None
    DOWNLOADED_PATH='downloaded'

class DevelopmentConfig(Config):
    FFMPEG_PATH='c:\\dev\\private_dev\\ffmpeg-2025-12-04-git-d6458f6a8b-full_build\\bin\\ffmpeg.exe'

class ProductionConfig(Config):
    DOWNLOADED_PATH='/var/YTD/Downloaded'
