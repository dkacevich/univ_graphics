import cv2
import numpy as np
from PIL import Image

# Завантаження зображення
image = cv2.imread('picture.jpg', cv2.IMREAD_GRAYSCALE)

# Визначення ядра фільтра (горизонтальні краї)
kernel = np.array([[ 1,  1,  1], 
                   [ 0,  0,  0],
                   [-1, -1, -1]])

# Застосування фільтра (отримання масиву пікселів)
filtered_image = cv2.filter2D(image, -1, kernel)

# Показ результату
Image.fromarray(filtered_image).show()





