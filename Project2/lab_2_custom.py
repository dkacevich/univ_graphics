from PIL import Image
import numpy as np

def apply_directed_filter(image_path):
    # Відкриття зображення
    image = Image.open(image_path).convert("L")

    # Ядро фільтра для горизонтальних ліній
    kernel = [[1, 1, 1],
              [0, 0, 0],
              [-1, -1, -1]]

    # Розмірів зображення
    width, height = image.size

    # Зображення в масив
    pixels = np.array(image)

    # Пустий масив для результату
    new_pixels = np.zeros_like(pixels)

    # Застосування фільтра
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            sum = 0
            for ky in range(-1, 2):
                for kx in range(-1, 2):
                    sum += kernel[ky + 1][kx + 1] * pixels[y + ky, x + kx]
            new_pixels[y, x] = min(max(sum, 0), 255)

    # Створення нового зображення з оброблених пікселів
    return Image.fromarray(new_pixels)



# Приклад використання
filtered_image = apply_directed_filter("picture.jpg")
filtered_image.show()
