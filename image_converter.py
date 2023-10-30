from helpers import *
from image_tool import ImageTool


def convert_image_format():
    current_image_list = []
    is_multiple = get_user_info("Multiple image converting: y/n")
    do_loop = check_yes_input(is_multiple)

    def add_info_to_image_list(image_list: list):
        while True:

            source = ImageTool.get_source_path("Type image filename in current folder:")

            if len(source) == 0:
                print("This image not exists")
                continue

            for info in image_list:
                if info.get('source') == source:
                    print("This image already selected")

                    if check_yes_input(get_user_info("Want to continue? y/n")):
                        continue
                    else:
                        return

            break

        while True:

            try:
                destination = ImageTool.get_destination_path()
                break

            except IndexError:
                print("You typed wrong filename")

            except ValueError as value_error:
                print(value_error)

        image_list.append({
            "source": source,
            "destination": destination
        })

    if not do_loop:
        add_info_to_image_list(current_image_list)
    while do_loop:
        add_info_to_image_list(current_image_list)

        enough = get_user_info("Enough? y/n")
        if check_yes_input(enough):
            break

    try:
        for data in current_image_list:
            ImageTool.convert_format(data['source'], data['destination'])

        print("Success")
    except ValueError as error:
        print(error)
    except OSError as error:
        print(error)
