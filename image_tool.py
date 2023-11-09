from pathlib import Path
from math import *
from PIL import Image, ImageEnhance
from PIL.Image import Resampling

from helpers import get_user_info, create_dir
from image_format import ImageFormat


# Class for grouping image manipulations
class ImageTool:

    # Just converting format
    @staticmethod
    def convert_format(source, destination):
        image = Image.open(source)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        create_dir(destination)

        image.save(destination)

    # Resizing image
    @staticmethod
    def resize_image(source, destination, width: int, height: int):
        image = Image.open(source)
        ratio = image.width / image.height

        if width == 0:
            width = height * ratio
        if height == 0:
            height = width / ratio

        image = image.resize((int(width), int(height)), Resampling.BOX)

        create_dir(destination)

        image.save(destination)

    # Converting color in image
    @staticmethod
    def convert_color(source, destination, source_color: tuple, result_color: tuple):
        image = Image.open(source)
        data = image.getdata()

        new_data = []

        for item in data:
            if item[:3] == source_color:
                new_data.append(result_color + item[3:])
            else:
                new_data.append(item)

        image.putdata(new_data)

        create_dir(destination)

        image.save(destination)

    # Adjusting color balance
    @staticmethod
    def adjust_color_balance(source, destination, red_factor, green_factor, blue_factor):
        image = Image.open(source)

        r, g, b = image.split()

        r = r.point(lambda i: i * red_factor)
        g = g.point(lambda i: i * green_factor)
        b = b.point(lambda i: i * blue_factor)

        image = Image.merge('RGB', (r, g, b))

        create_dir(destination)

        image.save(destination)



    # Change image transparency
    @staticmethod
    def change_transparency(source, destination, transparency):
        image = Image.open(source)
        if image.mode != 'RGB':
            image = image.convert('RGB')
               
                
        image.putalpha(transparency)
        
        create_dir(destination)
        
        image.save(destination, 'PNG')



    # Split image into parts
    # Currenty only divide width
    @staticmethod
    def split_to_parts(source, destination, parts):
        image = Image.open(source)
        format = image.format

        width, height = image.size
        part_width = width // parts
        images = []

        for i in range(parts):
            images.append(
                image.crop((i*part_width, 0, (i+1)*part_width, height))
            )      

        #TODO Cropping by width & height at same time
        # part_height = height // parts

        create_dir(destination)
        
        for i, image in enumerate(images):
            image.save(f"{destination}/part_{i}.{format}")
            


    # Remove area from image
    @staticmethod
    def remove_area(source, destination, area):
        image = Image.open(source).convert("RGBA")
        
        image.paste(Image.new('RGBA', (area[2]-area[0], area[3]-area[1])), area)

        create_dir(destination)
        
        image.save(destination, "PNG")
    
        
    # Remove outside area from image
    @staticmethod
    def remove_area_outside(source, destination, area):
        image = Image.open(source).convert("RGBA")

        try: 
            mask = Image.new('L', image.size, color='black')
            mask.paste(Image.new('L', area[2:], color='white'), area[:2])
            image.putalpha(mask)


            create_dir(destination)
            
            image.save(destination, "PNG")        
        except ValueError:
            print("Something goes wrong")
       
       
    # Change contract in image
    @staticmethod
    def change_contrast(source, destination, factor):
        image = Image.open(source)

        # Use Enhancer
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(factor)

        create_dir(destination)
        
        enhanced_image.save(destination)
            
     



    # Get correct source image path
    @staticmethod
    def get_source_path(message=None, not_found_message=None) -> str:

        while True:
            source = get_user_info(message or "Type image path:")
            path = Path(source)
            if path.exists() and path.is_file():
                break

            print(not_found_message or "Image not found")

        return source

    # Get correct destination image path
    @staticmethod
    def get_destination_path(message=None, ) -> str:

        while True:
            try:
                destination = get_user_info(message or
                                            "Type image filename with extension:")

                user_format = destination.split('.')[1]
                if not ImageFormat.accepted_value(user_format):
                    raise ValueError("Typed image format is not supported")

                break

            except IndexError:
                print("You typed wrong filename")

            except ValueError as value_error:
                print(value_error)

        return destination

