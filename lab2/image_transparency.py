from helpers import get_user_info
from image_tool import ImageTool


def transparent_image():
    source_path = ImageTool.get_source_path()
    destination_path = ImageTool.get_destination_path()

    while True:
        try:
            transparancy = int(get_user_info("Type transparency, it can be from 0 (completely transparent) to 255 (completely opaque)"))

            if transparancy < 0 and transparancy > 255:
                raise ValueError()

            break
        except ValueError:
            print("You typped wrong value")



    ImageTool.change_transparency(source_path, destination_path, transparancy)
