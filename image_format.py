from enum import Enum

class ImageFormat(Enum):
    JPG = "jpg"
    JPEG = "jpeg"
    PNG = "png"
    GIF = "gif"
    BMP = "bmp"
    
    def accepted_value(value: str) -> bool:
        return value in ImageFormat
    
    