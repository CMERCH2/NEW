import pygame
pygame.init()


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

def main():
    text = open_file()
    draw()



if __name__ == "__main__":
    main()
