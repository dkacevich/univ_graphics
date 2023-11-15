from helpers import get_user_info
from image_tool import ImageTool


def image_merge():
    first_image_path = ImageTool.get_source_path("Type path for first image")
    second_image_path = ImageTool.get_source_path("Type path for second image")
    destination_path = ImageTool.get_destination_path()

    while True:
        try:
            direction = get_user_info("Type join direction (horizontal - h, vertical - v):").lower()

            if direction != "h" and direction != "v":
                raise ValueError()

            break
        except ValueError:
            print("You typped wrong direction")



    ImageTool.merge_images(first_image_path, second_image_path, destination_path, direction)
