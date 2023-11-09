from helpers import get_user_info
from lab2.image_contrast import change_contrast
from lab2.image_removing_area import remove_area
from lab2.image_removing_area_outside import remove_area_outside
from lab2.image_splitting import split_into_parts
from lab2.image_transparency import transparent_image
from lab1.adjust_color_balance import adjust_color_balance
from lab1.image_color_converter import convert_image_color
from lab1.image_converter import convert_image_format
from lab1.image_resizer import resize_image


def main_menu():
    print("Program menu")

    print("\n")
    print("Lab 1:")
    print("1. Convert image format")
    print("2. Resize image")
    print("3. Change color")
    print("4. Adjust color balance")
    
    
    print("\n")
    print("Lab 2:")
    print("5. Change image transparancy")
    print("6. Split image into parts")
    print("7. Remove image area")
    print("8. Remove image outside area")
    print("9. Increase image contrast")
    
    
    
    print("\n")
    print("100. Exit")


# Menu
def run_menu():
    while True:
        main_menu()
        choice = get_user_info("Enter your choice:")

        # Lab 1
        if choice == "1":
            convert_image_format()
        elif choice == "2":
            resize_image()
        elif choice == "3":
            convert_image_color()
        elif choice == "4":
            adjust_color_balance()
            
        # Lab 2
        elif choice == "5":
            transparent_image()
        elif choice == "6":
            split_into_parts()
            
        elif choice == "7":
            remove_area()
        elif choice == "8":
            remove_area_outside()
            
        elif choice == "9":
            change_contrast()
        
        
        elif choice == "100":
            print("Exiting program...")
            break


if __name__ == "__main__":
    run_menu()
