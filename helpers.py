from pathlib import Path


def get_user_info(message: str) -> str:
    return input(message + " ")


def check_yes_input(input: str) -> bool:
    return input.lower() in ["y", "yes"]


def create_dir(path: str):
    path = Path(path)
    if not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)


def is_valid_rgb(color) -> bool:
    if len(color) != 3:
        return False

    for value in color:
        if not (0 <= value <= 255):
            return False

    return True
