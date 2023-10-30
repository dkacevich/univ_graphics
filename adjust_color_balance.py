from helpers import get_user_info
from image_tool import ImageTool


def adjust_color_balance():
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

            red_factor = float(get_user_info("Type coefficient for RED adjustment (1.0 by default)") or 1.0)
            green_factor = float(get_user_info("Type coefficient for GREEN adjustment (1.0 by default)") or 1.0)
            blue_factor = float(get_user_info("Type coefficient for BLUE adjustment (1.0 by default)") or 1.0)

            break
        except ValueError:
            print("You typped wrong value")

    ImageTool.adjust_color_balance(path, destination, red_factor, green_factor, blue_factor)
