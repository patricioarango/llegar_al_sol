import pygame
def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def text_objectsColor(text, font,color):
    textSurface = font.render(text, True, color)
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
        TextRect.center = ((1200 / 2), (150))
        screen.blit(TextSurf, TextRect)

        mediumText = pygame.font.Font('space_age.ttf', 40)
        texto = mediumText.render('¿estas listo?', False,(173,20,87))
        screen.blit(texto, (200,250))

        smallText = pygame.font.Font('Ranchers-Regular.ttf', 50)
        TextSurf2, TextRect2 = text_objectsColor("Tres Niveles. Varios Enemigos. Diferentes objetivos.", smallText,(69,39,160))
        TextRect2.center = ((1200 / 2), (470))
        screen.blit(TextSurf2, TextRect2)
        TextSurf2, TextRect2 = text_objectsColor( "Una hazaña que solo un verdadero gamer puede lograr", smallText,(83,109,254))
        TextRect2.center = ((1200 / 2), (525))
        screen.blit(TextSurf2, TextRect2)

        smallText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf2, TextRect2 = text_objects("Presioná cualquier tecla para empezar", smallText)
        TextRect2.center = ((1200 / 2), (700))
        screen.blit(TextSurf2, TextRect2)
        pygame.display.update()
