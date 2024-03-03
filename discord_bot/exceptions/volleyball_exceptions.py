class ImageNotFoundException(Exception):
    def __init__(self, image_type: str) -> None:
        self.message = f"'{image_type}' image not found"
        super().__init__(self.message)

class DateNotFoundException(Exception):
    def __init__(self, category: str) -> None:
        self.message = f"Could not extract last updated date for '{category}'"
        super().__init__(self.message)