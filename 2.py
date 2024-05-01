from PIL import Image
image = Image.open("laba7.jpg")

res_img2 = image.reduce(3)
res_img2.save('laba.jpg')

a = image.transpose(Image.FLIP_LEFT_RIGHT)
b = image.transpose(Image.FLIP_TOP_BOTTOM)
a.save('labaflip.jpg')
b.save('lababotton.jpg')

