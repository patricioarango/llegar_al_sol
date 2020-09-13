import pygame,time
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def game_intro(screen):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            #ingresamos al juego
            if event.type == pygame.KEYDOWN:
                intro = False

        screen.fill((255,255,255))
        largeText = pygame.font.Font('space_age.ttf', 90)
        TextSurf, TextRect = text_objects("Llegar al Sol", largeText)
        TextRect.center = ((1200 / 2), (600 / 2))
        screen.blit(TextSurf, TextRect)
        smallText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf2, TextRect2 = text_objects("Presioná cualquier tecla para empezar", smallText)
        TextRect2.center = ((1200 / 2), (600))
        screen.blit(TextSurf2, TextRect2)
        pygame.display.update()

def gameOver(screen):
    for img in ["gameover1.png", "gameover2.png", "gameover3.png", "gameover4.png"]:
        image = pygame.image.load(img)
        screen.blit(image, (0, 0))
        pygame.display.update()
        time.sleep(0.05)
