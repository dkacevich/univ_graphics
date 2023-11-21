from helpers import get_folder_path, get_user_info
from image_tool import ImageTool


def split_into_parts():
    source_path = ImageTool.get_source_path()
    destination_path = get_folder_path("Type folder path for storing parts")

    while True:
        try:
            parts_count = int(get_user_info("Type quantity parts to split your image"))

            if parts_count < 0:
                raise ValueError()

            break
        except ValueError:
            print("You typped wrong value")



    ImageTool.split_to_parts(source_path, destination_path, parts_count)
