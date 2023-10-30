from helpers import get_user_info, is_valid_rgb
from image_tool import ImageTool


def convert_image_color():
    source_path = ImageTool.get_source_path()
    destination_path = ImageTool.get_destination_path()

    while True:
        try:
            source_color = tuple(map(int, get_user_info("Type RGB color to be replaced (space separation):").split()))
            result_color = tuple(map(int, get_user_info("Type RGB color to replace (space separation):").split()))

            if not is_valid_rgb(source_color) or not is_valid_rgb(result_color):
                raise ValueError()

            break
        except ValueError:
            print("You typped wrong value")

    ImageTool.convert_color(source_path, destination_path, source_color, result_color)
