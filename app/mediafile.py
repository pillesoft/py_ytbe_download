from os import path

class MediaFile:

    _url: str
    _head: str
    _tail: str
    _ext: str
    _error_code: int
    _error_descr: str

    def __init__(self, url):
        self._url = url

    @property
    def Url(self):
        return self._url

    @Url.setter
    def Url(self, value):
        self._url = value

    @property
    def Head(self):
        return self._head

    @Head.setter
    def Head(self, value):
        self._head = value

    @property
    def Tail(self):
        return self._tail

    @Tail.setter
    def Tail(self, value):
        self._tail = value

    @property
    def Ext(self):
        return self._ext

    @Ext.setter
    def Ext(self, value):
        self._ext = value

    @property
    def ErrorCode(self):
        return self._error_code

    @ErrorCode.setter
    def ErrorCode(self, value):
        self._error_code = value

    @property
    def ErrorDescription(self):
        return self._error_descr

    @ErrorDescription.setter
    def ErrorDescription(self, value):
        self._error_descr = value

    @property
    def FilePath(self):
        return path.join("..", self._head, self.FileExt)
    
    @property
    def FileExt(self):
        return "{}{}".format(self._tail, self._ext)
    