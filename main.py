from PIL import Image, ImageDraw

def main():
    try:
        inputimagename = input('Image name : ')
        image = Image.open(inputimagename)

        width, height = image.size
        ratio = width/height
        if ratio != 0.5625:
            print('Not 9:16')
            return
        for x in range(6):
            morepos = (height/6) * (x+1)
            pos = (height/6) * x
            imgcache = image.crop((0, pos, width, morepos))
            imgcache.resize((1,1))
            color = imgcache.getpixel((0,0))
            x0 = (width/2.66)
            y0 = (height/5.2) + (x * ((height/11.4) + 23))
            x1 = x0 + (width/4)
            y1 = y0 + (height/11.4)
            draw = ImageDraw.Draw(image)
            draw.rectangle((x0 , y0 , x1 ,y1), fill=color, outline=None)
            del draw
        filename = inputimagename + "_output.jpg"
        image.save(filename)
    except IOError: 
        pass

if __name__ == "__main__": 
    main() 

