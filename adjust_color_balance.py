from helpers import get_user_info
from image_tool import ImageTool


def adjust_color_balance():
    source_path = ImageTool.get_source_path()
    destination_path = ImageTool.get_destination_path()

    while True:
        try:
            red_factor = float(get_user_info("Type coefficient for RED adjustment (1.0 by default)") or 1.0)
            green_factor = float(get_user_info("Type coefficient for GREEN adjustment (1.0 by default)") or 1.0)
            blue_factor = float(get_user_info("Type coefficient for BLUE adjustment (1.0 by default)") or 1.0)

            break
        except ValueError:
            print("You typped wrong value")

    ImageTool.adjust_color_balance(
        source_path,
        destination_path,
        red_factor,
        green_factor,
        blue_factor
    )
