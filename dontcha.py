import PIL
from PIL import Image, ImageFont, ImageDraw
import random
import string

def main():
    #Right now this is for simple tests
    dontcha = Dontcha()
    i = Image.new('RGB',(600,200), color='red')

    draw = ImageDraw.Draw(i)
    draw.text((10,10), dontcha.generateWord(), font=dontcha.font)

    i.save('test.jpg', 'JPEG')
    #print(dir(dontcha._getText('apple')))#.save('test.jpg', 'JPEG')

class Dontcha():
    def __init__(self):
        #Creates a dontcha objet
        self.font = PIL.ImageFont.truetype('Pixel-UniCode.ttf', 100)
        self._buildUnicodeCharList()

    def generateWord(self):
        """Creates a new word between 10 and 20 characters in length using 
        characters from string.ascii_letters
        """
        length = random.randint(10,20)

        word = ""

        for i in range(length):
            c = random.choice(string.ascii_letters)
            word += c

        return word

    def _buildUnicodeCharList(self):
        """Populates self.chars with the numeric representation of valid
        unicode characters. This is done manually because unicode has undefined
        gaps and blank characters that should not be used, so a simple rarnge
        will not work.
        """
        self.chars = list(range(0x21, 0x7E)) + \
                list(range(0xA1, 0xAC))


if __name__ == "__main__":
    main()
