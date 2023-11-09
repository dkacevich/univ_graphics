from helpers import get_user_info
from image_tool import ImageTool


def change_contrast():
    source_path = ImageTool.get_source_path()
    destination_path = ImageTool.get_destination_path()

    while True:
        try:
            factor = float(get_user_info("Type contrast factor (must be bigger than 1.0)"))

            if factor < 1:
                raise ValueError()

            break
        except ValueError:
            print("You typped wrong value")



    ImageTool.change_contrast(source_path, destination_path, factor)
