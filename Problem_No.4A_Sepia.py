def sepia(oldPixel):
    red = oldPixel.getRed()
    green = oldPixel.getGreen()
    blue = oldPixel.getBlue()


    newR = int(R * 0.393 + G * 0.769 + B * 0.189)
    newG = int(R * 0.349 + G * 0.686 + B * 0.168)
    newB = int(R * 0.272 + G * 0.534 + B * 0.131)

    newPixel = Pixel(newR, newG, newB)
    return newPixel
