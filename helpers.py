def get_user_info(message: str) -> str:
    return input(message + " ")


def check_yes_input(input: str) -> bool:
    return input.lower() in ["y", "yes"]


def is_image_format_correct(input: str) -> bool:
    return input.lower() in ["jpg", "jpeg", "png", "gif"]


def is_valid_rgb(color) -> bool:
    if len(color) != 3:
        return False

    for value in color:
        if not (0 <= value <= 255):
            return False

    return True
