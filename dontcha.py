import PIL
from PIL import Image, ImageFont, ImageDraw

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

    def _getText(self, text):
        return self.font.getmask(text)

if __name__ == "__main__":
    main()
