from helpers import get_user_info, is_valid_rgb
from image_tool import ImageTool


def convert_image_color():
    while True:
        path = ImageTool.get_source_path()

        if len(path) != 0:
            break

        print("Image not found")

    while True:
        try:
            destination = ImageTool.get_destination_path()
            break

        except IndexError:
            print("You typed wrong filename")

        except ValueError as value_error:
            print(value_error)

    while True:
        try:
            source_color = tuple(map(int, get_user_info("Type RGB color to be replaced (space separation):").split()))
            result_color = tuple(map(int, get_user_info("Type RGB color to replace (space separation):").split()))

            if not is_valid_rgb(source_color) or not is_valid_rgb(result_color):
                raise ValueError()

            break
        except ValueError:
            print("You typped wrong value")

    ImageTool.convert_color(path, destination, source_color, result_color)
