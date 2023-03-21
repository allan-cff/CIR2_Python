from PIL import Image


def creer_drapeau_francais(larg=450, haut=300):
    img = Image.new("RGB", (larg, haut), (0, 0, 255))
    for x in range(int(larg/3), int(2*larg/3)):
        for y in range(0, haut):
            img.putpixel((x, y), (255, 255, 255))
    for x in range(int(2*larg/3), int(larg)):
        for y in range(0, haut):
            img.putpixel((x, y), (255, 0, 0))
    return img


#image = creer_drapeau_francais()
#image.show()


def creer_degrade_gris(larg=256, haut=256):
    img = Image.new("RGB", (larg, haut), (0, 0, 0))
    for y in range(0, haut):
        for x in range(0, larg):
            val = int(255*y/haut)
            img.putpixel((x, y), (val, val, val))
    return img


#image = creer_degrade_gris()
#image.show()


def miroir(image):
    larg, haut = image.size
    newImage = Image.new("RGB", (larg, haut), (0, 0, 0))
    for x in range(0, larg):
        for y in range(0, haut):
            pixel = image.getpixel((larg - 1 - x, y))
            newImage.putpixel((x, y), pixel)
    return newImage


#lena = Image.open("lena.png")
#lena = miroir(lena)
#lena.show()
#lena.save("lena_miroir.png")


def negatif(image):
    larg, haut = image.size
    newImage = Image.new("RGB", (larg, haut), (0, 0, 0))
    for x in range(0, larg):
        for y in range(0, haut):
            r, g, b = image.getpixel((x, y))
            newImage.putpixel((x, y), (255-r, 255-g, 255-b))
    return newImage


#lena = Image.open("lena.png")
#lena = negatif(lena)
#lena.show()


def niveaux_de_gris(image):
    larg, haut = image.size
    newImage = Image.new("RGB", (larg, haut), (0, 0, 0))
    for x in range(0, larg):
        for y in range(0, haut):
            r, g, b = image.getpixel((x, y))
            l = int((r + g + b)/3)
            newImage.putpixel((x, y), (l, l, l))
    return newImage


#lena = Image.open("lena.png")
#lena = niveaux_de_gris(lena)
#lena.show()


def rotation90(image, sens_trigo):
    larg, haut = image.size
    newImage = Image.new("RGB", (haut, larg), (0, 0, 0))
    for x in range(0, larg):
        for y in range(0, haut):
            pix = image.getpixel((x, y))
            newImage.putpixel((y if sens_trigo else haut - 1 - y, x), pix)
    return newImage


#lena = Image.open("lena.png")
#lena = rotation90(lena, True)
#lena.show()
#lena = Image.open("lena.png")
#lena = rotation90(lena, False)
#lena.show()


def contours(image, s):
    larg, haut = image.size
    newImage = Image.new("RGB", (larg, haut), (0, 0, 0))
    for x in range(0, larg):
        for y in range(0, haut):
            G = image.getpixel((max(0, x-1), y))
            H = image.getpixel((x, max(0, y-1)))
            D = image.getpixel((min(larg-1, x+1), y))
            B = image.getpixel((x, min(haut-1, y+1)))
            v = abs(int(sum(G)/3)-int(sum(D)/3)) + abs(int(sum(H)/3)-int(sum(B)/3))
            val = 0 if v > s else 255
            newImage.putpixel((x, y), (val, val, val))
    return newImage


lena = Image.open("lena.png")
lena = contours(lena, 50)
lena.show()