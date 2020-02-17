import pytesseract
from PIL import Image


def covert_img(img, threshold):
    img = img.convert('L')
    pixels = img.load()
    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] > threshold:
                pixels[x, y] = 255
            else:
                pixels[x, y] = 0
            return img


mypic = Image.open('e.jpg')
mypic = covert_img(mypic, 80)
mypic.show()
mypic.save('convertimg.jpg')
res = pytesseract.image_to_string(mypic)
print(res)
