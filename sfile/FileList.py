from .FileDetail import FileDetail


class FileList():
    def __init__(self, name, size, url):
        self.name = name
        self.size = size
        self.url = url

    def get_detail(self, url=None):
        if not url:
            url = self.url
        return FileDetail(url)
