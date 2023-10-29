from helpers import *
from pathlib import Path
from image_format import ImageFormat
from image_tool import ImageTool

def convert_image_format():
    image_list = []
    is_multiple = get_user_info("Multiple image converting: y/n")
    do_loop = check_yes_input(is_multiple)


    def add_info_to_image_list(image_list: list):
        while True:
            source = get_user_info("Type image filename in current folder:")
            
            for info in image_list:
                if info.get('source') == source:
                    print("This image already selected")
                    
                    if check_yes_input(get_user_info("Want to continue? y/n")):
                        continue
                    else:
                        return
            
            if not Path(source).exists():
                print("This image not exists")
            else:
                break     
        
        while True:
            destination = get_user_info("Type image filename with extension")
            
            try:
                format = destination.split('.')[1]
                if not ImageFormat.accepted_value(format):
                    raise ValueError("Typed image format is not supported")
                
                break
                                       
            except IndexError as error:
                print("You typed wrong filename")
        
            except ValueError as error:
                print(error)
        
        image_list.append({
            "source": source,
            "destination": destination
        })

    if do_loop == False:
        add_info_to_image_list(image_list)
    while do_loop:
        add_info_to_image_list(image_list)
        
        enough = get_user_info("Enough? y/n")
        if check_yes_input(enough):
            break
        

    try:
        for data in image_list:
            ImageTool.convert_format(data['source'], data['destination'])
            
        print("Success")
    except ValueError as error:
        print(error)
    except OSError as error:
        print(error)
        
