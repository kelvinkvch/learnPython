from PIL import Image
import subprocess


def cleanfile(filepath, newfilepath):
    img = Image.open(filepath)
    img = img.point(lambda x: 0 if x < 145 else 255)
    img.save(newfilepath)
    subprocess.call(['tesseract', newfilepath, 'output'])
    outputfile = open('output.txt', 'r', encoding='utf8')
    print(outputfile.read())
    outputfile.close()


cleanfile('text.png', 'text_2_clean.png')
