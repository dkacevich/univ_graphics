from pathlib import Path

from PIL import Image

from helpers import get_user_info
from image_format import ImageFormat


class ImageTool:

    @staticmethod
    def convert_format(source, destination):
        image = Image.open(source)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        destination_path = Path(destination)
        if not destination_path.parent.exists():
            destination_path.parent.mkdir(parents=True, exist_ok=True)

        image.save(destination)

    @staticmethod
    def resize_image(source, destination, width: int, height: int):
        image = Image.open(source)
        ratio = image.width / image.height

        if width == 0:
            width = height * ratio
        if height == 0:
            height = width / ratio

        image = image.resize((int(width), int(height)))

        destination_path = Path(destination)
        if not destination_path.parent.exists():
            destination_path.parent.mkdir(parents=True, exist_ok=True)

        image.save(destination)

    @staticmethod
    def convert_color(source, destination, source_color: tuple, result_color: tuple):
        image = Image.open(source)
        data = image.getdata()

        new_data = []

        for item in data:
            if item[:3] == source_color:
                new_data.append(result_color + item[3:])
            else:
                new_data.append(item)

        image.putdata(new_data)

        destination_path = Path(destination)
        if not destination_path.parent.exists():
            destination_path.parent.mkdir(parents=True, exist_ok=True)

        image.save(destination)

    @staticmethod
    def adjust_color_balance(source, destination, red_factor, green_factor, blue_factor):
        image = Image.open(source)

        r, g, b = image.split()

        r = r.point(lambda i: i * red_factor)
        g = g.point(lambda i: i * green_factor)
        b = b.point(lambda i: i * blue_factor)

        image = Image.merge('RGB', (r, g, b))

        destination_path = Path(destination)
        if not destination_path.parent.exists():
            destination_path.parent.mkdir(parents=True, exist_ok=True)

        image.save(destination)

    @staticmethod
    def get_source_path(message=None) -> str:
        source = get_user_info(message or "Type image path")

        if not Path(source).exists():
            return ""

        return source

    @staticmethod
    def get_destination_path(message=None) -> str:
        destination = get_user_info(message or
                                    "Type image filename with extension")

        user_format = destination.split('.')[1]
        if not ImageFormat.accepted_value(user_format):
            raise ValueError("Typed image format is not supported")

        return destination
