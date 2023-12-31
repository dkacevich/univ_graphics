from pathlib import Path

from PIL import Image, ImageEnhance, ImageDraw, ImageFont
from PIL.Image import Resampling

from helpers import get_user_info, create_dir
from image_format import ImageFormat


# Class for grouping image manipulations
class ImageTool:
    result = []

    # Just converting format
    @staticmethod
    def convert_format(source, destination):
        image = Image.open(source)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        ImageTool.save_image(image, destination)

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

        ImageTool.save_image(image, destination)

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

        ImageTool.save_image(image, destination)

    # Adjusting color balance
    @staticmethod
    def adjust_color_balance(source, destination, red_factor, green_factor, blue_factor):
        image = Image.open(source)

        r, g, b = image.split()

        r = r.point(lambda i: i * red_factor)
        g = g.point(lambda i: i * green_factor)
        b = b.point(lambda i: i * blue_factor)

        image = Image.merge('RGB', (r, g, b))

        ImageTool.save_image(image, destination)

    # Change image transparency
    @staticmethod
    def change_transparency(source, destination, transparency):
        image = Image.open(source)
        if image.mode != 'RGB':
            image = image.convert('RGB')

        image.putalpha(transparency)

        ImageTool.save_image(image, destination, format="PNG")

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
                image.crop((i * part_width, 0, (i + 1) * part_width, height))
            )

        # TODO Cropping by width & height at same time
        # part_height = height // parts

        create_dir(destination)

        for i, image in enumerate(images):
            image_path = f"{destination}/part_{i}.{format}"

            ImageTool.result.append(image_path)

            image.save(image_path)

    # Remove area from image
    @staticmethod
    def remove_area(source, destination, area):
        image = Image.open(source).convert("RGBA")

        image.paste(Image.new('RGBA', (area[2] - area[0], area[3] - area[1])), area)

        ImageTool.save_image(image, destination, format="PNG")

    # Remove outside area from image
    @staticmethod
    def remove_area_outside(source, destination, area):
        image = Image.open(source).convert("RGBA")

        try:
            mask = Image.new('L', image.size, color='black')
            mask.paste(Image.new('L', area[2:], color='white'), area[:2])
            image.putalpha(mask)

            ImageTool.save_image(image, destination, format="PNG")
        except ValueError:
            print("Something goes wrong")

    # Change contract in image
    @staticmethod
    def change_contrast(source, destination, factor):
        image = Image.open(source)

        # Use Enhancer
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(factor)

        ImageTool.save_image(enhanced_image, destination)

    # Merge 2 Images into 1
    @staticmethod
    def merge_images(first_source, second_source, destination, direction):
        first_image = Image.open(first_source)
        second_image = Image.open(second_source)

        # Визначення розмірів зображень
        width1, height1 = first_image.size
        width2, height2 = second_image.size

        # Об'єднання зображень
        if direction == 'h':
            # Горизонтальне об'єднання
            new_width = width1 + width2
            new_height = max(height1, height2)
            new_image = Image.new('RGB', (new_width, new_height))
            new_image.paste(first_image, (0, 0))
            new_image.paste(second_image, (width1, 0))
        else:
            # Вертикальне об'єднання
            new_width = max(width1, width2)
            new_height = height1 + height2
            new_image = Image.new('RGB', (new_width, new_height))
            new_image.paste(first_image, (0, 0))
            new_image.paste(second_image, (0, height1))

        ImageTool.save_image(new_image, destination)

    @staticmethod
    def add_watermark(source, destination, watermark_text, position, opacity, font_size, rotate_angle, color):

        image = Image.open(source).convert("RGBA")

        font = ImageFont.truetype("lab3/Arial.ttf", font_size)
        text_image = Image.new('RGBA', tuple(x * 2 for x in image.size), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)
        draw.text(position, watermark_text, fill=color + (int(255 * opacity),), font=font)

        rotated_text_image = text_image.rotate(rotate_angle)

        watermark_layer = Image.new("RGBA", image.size)

        watermark_layer.paste(rotated_text_image, (0, 0), rotated_text_image)

        watermarked = Image.alpha_composite(image, watermark_layer)

        ImageTool.save_image(watermarked, destination, format="PNG")

    @staticmethod
    def save_image(image, destination, format=None):
        create_dir(destination)

        ImageTool.result.append(destination)

        image.save(destination, format)

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
