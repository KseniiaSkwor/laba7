from PIL import Image
image = Image.open("laba7.jpg")
image2 = Image.open("vz.png")

image.paste(image2, (250, 100), image2)
image.show()

