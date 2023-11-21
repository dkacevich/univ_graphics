from helpers import get_user_info
from image_tool import ImageTool


def remove_area_outside():
    source_path = ImageTool.get_source_path()
    destination_path = ImageTool.get_destination_path()

    while True:
        try:
            area = get_user_info("Type area from image (separate by space) (left, top, width, height):")

            area = tuple(map(int, area.split()))

            break
        except ValueError:
            print("You typped wrong value")
        except IndexError:
            print("You typped wrong value")

    ImageTool.remove_area_outside(source_path, destination_path, area)
