from helpers import get_user_info
from image_tool import ImageTool


def resize_image():
    source_path = ImageTool.get_source_path()
    destination_path = ImageTool.get_destination_path()

    while True:
        try:
            width = int(get_user_info("Type new width (0 for save original ratio):"))
            height = int(get_user_info("Type new height (0 for save original ratio):"))

            break
        except ValueError:
            print("You typped wrong value")

    ImageTool.resize_image(source_path, destination_path, width, height)
