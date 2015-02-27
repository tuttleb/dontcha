import PIL
from PIL import Image, ImageFont, ImageDraw
import random

def main():
    dontcha = Dontcha()
    i = Image.new('RGB',(100,100), color='red')

    draw = ImageDraw.Draw(i)
    draw.text((10,10), 'test', font=dontcha.font)

    i.save('test.jpg', 'JPEG')
    #print(dir(dontcha._getText('apple')))#.save('test.jpg', 'JPEG')

class Dontcha():
    def __init__(self):
        self.font = PIL.ImageFont.truetype(filename='Pixel-UniCode.ttf')
        self._buildUnicodeCharList()

    def generateWord(self):
        length = random.randint(10,20)

        word = ""

        for i in range(length):
            c = chr(random.choice(self.chars))
            word += c

        return word

    def _buildUnicodeCharList(self):
        self.chars = list(range(0x21, 0x7E)) + \
                list(range(0xA1, 0xAC))


if __name__ == "__main__":
    main()
