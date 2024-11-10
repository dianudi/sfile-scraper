
class LockedFileException(Exception):
    def __init__(self):
        self.message = "File is locked"
        super().__init__(self.message)


class FileNotFoundException(Exception):
    def __init__(self):
        self.message = "File not found"
        super().__init__(self.message)
