import png
from PIL import Image

def convert(grid, rows, width):
    image = []
    gap = width // rows
    for row in reversed(grid):
        for j in range(gap):
            rowarr = ()
            for block in row:
                for i in range(gap):
                    rowarr = rowarr + block.color
            image.append(rowarr)


    return image


def save(grid, rows, width):
    image = convert(grid, rows, width)
    f = open('pixel.png', 'wb')
    w = png.Writer(width, width, greyscale=False)
    w.write(f, image)
    f.close()
    colorImage  = Image.open("./pixel.png")
    transposed  = colorImage.transpose(Image.ROTATE_270)
    transposed.save("./pixel.png")
