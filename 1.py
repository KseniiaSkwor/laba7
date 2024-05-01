from PIL import Image
image = Image.open("laba7.jpg")
image.show()

import os
file_info = os.stat('laba7.jpg')
file_size = file_info.st_size
print('Размер файла:', file_size, 'байт')

print("Формат фото: ", image.format)
print("Цветовая модель: ", image.mode)
