def get_user_info(message: str) -> str:
    return input(message + " ")

def check_yes_input(input: str) -> bool:
    return input.lower() in ["y", "yes"]


def is_image_format_correct(input: str) -> bool:
    return input.lower() in ["jpg", "jpeg", "png", "gif"]
