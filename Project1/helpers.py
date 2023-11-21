from pathlib import Path


def get_user_info(message: str) -> str:
    return input(message + " ")


def check_yes_input(input: str) -> bool:
    return input.lower() in ["y", "yes"]


def create_dir(path: str):
    
    is_file = len(path.split(".")) == 2
    
    path = Path(path)
    
    if is_file and not path.parent.exists():
        path.parent.mkdir(parents=True, exist_ok=True)
    
    if not is_file and not path.exists():
        path.mkdir(parents=True, exist_ok=True)


def is_valid_rgb(color) -> bool:
    if len(color) != 3:
        return False

    for value in color:
        if not (0 <= value <= 255):
            return False

    return True


def get_folder_path(message: str = None, error_message: str = None) -> str:
    
    while True:
        try:
            folder_path = get_user_info(message or "Type folder name")
        
            if len(folder_path.split('.')) > 1:
                raise ValueError("Type correct folder path")

            break
        except ValueError as error:
            print(error or error_message)
        
        
    return folder_path
    