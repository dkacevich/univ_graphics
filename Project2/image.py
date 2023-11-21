from PIL import Image
from matplotlib import pyplot as plt
import numpy as np


def display_color_image(img):
    img.show()

def display_brightness_matrix(img):
    img = img.convert("L")
    print(np.array(img))


def display_brightness_histogram(img):
    color_array = np.array(img)

    # Розділяємо кольорові канали
    r, g, b = color_array[:,:,0], color_array[:,:,1], color_array[:,:,2]

    # Будуємо гістограму для кожного кольорового каналу
    plt.figure(figsize=(10, 4))

    plt.subplot(1, 3, 1)
    plt.hist(r.ravel(), bins=256, color='Red', alpha=0.5)
    plt.title('Red Channel')
    plt.xlim([0, 256])

    plt.subplot(1, 3, 2)
    plt.hist(g.ravel(), bins=256, color='Green', alpha=0.5)
    plt.title('Green Channel')
    plt.xlim([0, 256])

    plt.subplot(1, 3, 3)
    plt.hist(b.ravel(), bins=256, color='Blue', alpha=0.5)
    plt.title('Blue Channel')
    plt.xlim([0, 256])

    plt.tight_layout()
    plt.show()


def display_binary_image(img):
    img = img.convert("L")
    gray_array = np.array(img)
    
    # Беремо середнє значення та порівнюємо з ним кожен піксель масиву
    threshold = gray_array.mean()
    binary_image = (gray_array > threshold) * 255
    
    Image.fromarray(binary_image.astype('uint8')).show()


def display_negative_image(img):
    img.convert('RGB').point(lambda x: 255 - x).show()
    
    
def display_gray_image(img):
    img.convert('L').show()


def display_gray_histogram(img):
    gray_array = np.array(img.convert('L'))
    
    plt.hist(gray_array.ravel(), bins=256, color='gray', alpha=0.5)
    plt.title("Histogram of Grayscale Image")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Frequency")
    plt.xlim([0, 256])
    plt.show()
    
    

image_path = 'picture.jpg'
image = Image.open(image_path)

while True:
        choice = input("\nВиберіть опцію:\n"
                       "1 - Вивести кольорове зображення\n"
                       "2 - Вивести на екран матриці значень яскравості зображення \n"
                       "3 - Вивести гістограму яскравості кольорового зображення\n\n\n"

                       "4 - Зміна кольоровості: бінаризація\n"
                       "5 - Зміна кольоровості: перехід до відтінків сірого\n"
                       "6 - Зміна кольоровості: негатив\n"
                       "7 - Побудова гістограми зображення в градаціях сірого\n"
                       "0 - Вийти\n"
                       "Ваш вибір: ")

        if choice == '1':
            display_color_image(image)
        elif choice == '2':
            display_brightness_matrix(image)
        elif choice == '3':
            display_brightness_histogram(image)
            
            
            
        elif choice == '4':
            display_binary_image(image)
        elif choice == '5':
            display_gray_image(image)
        elif choice == '6':
            display_negative_image(image)
        elif choice == '7':
            display_gray_histogram(image)
        elif choice == '0':
            break
        
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            
    