class ImageNotFoundException(Exception):
    def __init__(self, image_type):
        self.image_type = image_type
        self.message = f"{image_type} image not found"
        super().__init__(self.message)