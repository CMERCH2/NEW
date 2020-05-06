import pygame
import pickle
pygame.init()

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors)

def open_file():
    try:
        file = open("test.txt")
        full = file.read()
        return full
    finally:
        file.close()

def draw():

    win = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Pojal, razjal")



    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        win.fill((255,255,255))

        pygame.draw.rect(win, (128,128,128), (10, 10, 230, 40))
    #text1 = win.render("My text1",True,black)
        pygame.draw.rect(win, (100,100,100), (9, 9, 228, 38))
    #screen.blit(text, [20,20])

        pygame.draw.rect(win, (128,128,128), (260, 10, 230, 40))
    #tex2t = win.render("Open",True,black)
        pygame.draw.rect(win, (100,100,100), (259, 9, 228, 38))
    #screen.blit(text, [270,20])

        pygame.draw.rect(win, (128,128,128), (10, 60, 115, 40))
    #text3 = win.render("encode",True,black)
        pygame.draw.rect(win, (100,100,100), (9, 59, 114, 38))
    #screen.blit(text, [20,70])

        pygame.draw.rect(win, (128,128,128), (260, 60, 115, 40))
    #text4 = win.render("decode",True,black)
        pygame.draw.rect(win, (100,100,100), (259, 59, 114, 38))
    #screen.blit(text, [270,70])

        pygame.draw.rect(win, (128,128,128), (150, 60, 40, 40))
    #text5 = win.render("My text",True,black)
        pygame.draw.rect(win, (100,100,100), (149, 59, 39, 38))
    #screen.blit(text5, [140,70])

        pygame.draw.rect(win, (128,128,128), (400, 60, 40, 40))
        pygame.draw.rect(win, (100,100,100), (399, 59, 39, 38))

        pygame.draw.rect(win, (128,128,128), (10, 120, 480, 40))
        pygame.draw.rect(win, (100,100,100), (9, 119, 479, 39))


        pygame.draw.rect(win, (200,200,200), (10, 200, 480, 40))

        pygame.display.update()

    pygame.quit()
def counter(text):
    slovar = [0]*128
    for i in range(128):
        bits = ''
        b = i
        print(i)
        for j in range(8):
            bits = str(b%2) + bits
            b //= 2
        print(bits)
        symbol = text_from_bits(bits)
        gg = text.count(symbol)
        slovar[i] = gg
    slovar[0] = 0
    print(slovar)
    return slovar

def tree(slovar):
    def addsymbol(str, number):
        vivod = ''
        b = 0
        if str == "1":
            vivod = number + 'cc'
            return vivod
        elif str == '0':
            vivod == number + 'oo'
            return vivod
        elif len(str) == 1:
            return (str+number)
        else:

            for i in range(len(str)):

                if str[i] not in "01":
                    print(str[i])
                    if str[i+1] not in "01":
                        continue
                    vivod += str[b:i+1] + number
                    b = i+1
            vivod += str[b:]
            return vivod

    symbols = []
    symbols2 = []
    count = []
    count2 = []

    for i in range(128):
        if slovar[i]!=0:
            bits = ''
            b = i

            for j in range(8):
                bits = str(b%2) + bits
                b //= 2
            symbol = text_from_bits(bits)
            symbols.append(symbol)
            count.append(slovar[i])

    for i in range(len(count)):
        a = min(count)
        z = count.index(a)
        count2.append(a)
        symbols2.append(symbols[z])
        del count[z]
        symbols = symbols[:z] + symbols[z+1:]

    kount = len(count2)

    for i in range(kount-1):
        symbols2[1] = addsymbol(symbols2[0], '0') + addsymbol(symbols2[1], '1')
        symbols2 = symbols2[1:]
        count2[1] = count2[0] + count2[1]
        del count2[0]


        count = count2
        symbols = symbols2
        count2 = []
        symbols2 = []
        for i in range(len(count)):
            a = min(count)
            z = count.index(a)
            count2.append(a)
            symbols2.append(symbols[z])
            del count[z]
            symbols = symbols[:z] + symbols[z+1:]
        #print(symbols2, count2)
    print(symbols, count)
    print(symbols2, count2)
    symm = symbols2[0]
    return symm
def codir(code, text):
    count = len(code)
    lib = {}
    for i in range(2, count):
        if code[i] not in '01':
            if code[i+1] not in "01":
                continue
            lib[code[i]] = 
def otpravka(code):
    f = open('FILENAME.bin','wb')

    f.close()
    with open('FILENAME.bin', "wb") as file:
        pickle.dump(code, file)


    with open('FILENAME.bin', "rb") as file:
        name = pickle.load(file)

        print("Имя:", name)

def main():
    text = open_file()
    slovar = counter(text)
    code = tree(slovar)
    end = codir(code, text)
    otpravka(code)
    #draw()



if __name__ == "__main__":
    main()
