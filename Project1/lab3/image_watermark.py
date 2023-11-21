import math
import random
from helpers import get_user_info, is_valid_rgb
from image_tool import ImageTool


def add_watermark():
    source_path = ImageTool.get_source_path()
    destination_path = ImageTool.get_destination_path()

    while True:
        try:
            text = get_user_info("Type watermark text:")
            x_position = int(get_user_info("Type watermark x position:"))
            y_position = int(get_user_info("Type watermark y position:"))
            position = (x_position, y_position)
            opacity = float(get_user_info("Type watermark text opacity:"))
            font_size = int(get_user_info("Type watermark text font size:"))
            rotate_angle = float(get_user_info("Type watermark text rotate angle:"))
            color = tuple(map(int, get_user_info("Type RGB text color:").split()))

            if not is_valid_rgb(color):
                raise ValueError("Wrong color name")


            break
        except ValueError as error:
            print(error)


   
    ImageTool.add_watermark(
        source_path,
        destination_path,
        text,
        position,
        opacity,
        font_size,
        rotate_angle,
        color
    )
