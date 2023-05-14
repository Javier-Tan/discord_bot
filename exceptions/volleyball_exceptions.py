class ImageNotFoundException(Exception):
    def __init__(self):
        self.message = "Ranking image not found"
        super().__init__(self.message)