from adjust_color_balance import adjust_color_balance
from helpers import *
from image_color_converter import convert_image_color
from image_converter import convert_image_format
from image_resizer import resize_image


def main_menu():
    print("Program menu")
    print("1. Convert image format")
    print("2. Resize image")
    print("3. Change color")
    print("4. Adjust color balance")
    print("5. Exit")


def run_menu():
    while True:
        main_menu()
        choice = get_user_info("Enter your choice (1-4):")

        if choice == "1":
            convert_image_format()
        elif choice == "2":
            resize_image()
        elif choice == "3":
            convert_image_color()
        elif choice == "4":
            adjust_color_balance()
        elif choice == "5":
            print("Exiting program...")
            break


if __name__ == "__main__":
    run_menu()
