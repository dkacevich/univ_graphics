from helpers import get_user_info
from image_tool import ImageTool


def resize_image():
    while True:
        path = ImageTool.get_source_path()

        if len(path) != 0:
            break

        print("Image not found")

    while True:
        destination = get_user_info("Type destination folder path")

        if len(path) != 0:
            break

        print("Wrong path")

    while True:
        try:
            width = int(get_user_info("Type new width (0 for save original ratio):"))
            height = int(get_user_info("Type new height (0 for save original ratio):"))

            break
        except ValueError:
            print("You typped wrong value")

    ImageTool.resize_image(path, destination, width, height)
