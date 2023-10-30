from pathlib import Path

from PIL import Image

from helpers import get_user_info, create_dir
from image_format import ImageFormat


# Class for grouping image manipulations
class ImageTool:

    # Just converting format
    @staticmethod
    def convert_format(source, destination):
        image = Image.open(source)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        create_dir(destination)

        image.save(destination)

    # Resizing image
    @staticmethod
    def resize_image(source, destination, width: int, height: int):
        image = Image.open(source)
        ratio = image.width / image.height

        if width == 0:
            width = height * ratio
        if height == 0:
            height = width / ratio

        image = image.resize((int(width), int(height)))

        create_dir(destination)

        image.save(destination)

    # Converting color in image
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

        create_dir(destination)

        image.save(destination)

    # Adjusting color balance
    @staticmethod
    def adjust_color_balance(source, destination, red_factor, green_factor, blue_factor):
        image = Image.open(source)

        r, g, b = image.split()

        r = r.point(lambda i: i * red_factor)
        g = g.point(lambda i: i * green_factor)
        b = b.point(lambda i: i * blue_factor)

        image = Image.merge('RGB', (r, g, b))

        create_dir(destination)

        image.save(destination)

    # Get correct source image path
    @staticmethod
    def get_source_path(message=None, not_found_message=None) -> str:

        while True:
            source = get_user_info(message or "Type image path")
            path = Path(source)
            if path.exists():
                break

            print(not_found_message or "Image not found")

        return source

    # Get correct destination image path
    @staticmethod
    def get_destination_path(message=None, ) -> str:

        while True:
            try:
                destination = get_user_info(message or
                                            "Type image filename with extension")

                user_format = destination.split('.')[1]
                if not ImageFormat.accepted_value(user_format):
                    raise ValueError("Typed image format is not supported")

                break

            except IndexError:
                print("You typed wrong filename")

            except ValueError as value_error:
                print(value_error)

        return destination
