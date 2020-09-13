import pygame

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

class Niveles(object):
    def __init__(self,nivel):
        self.nivel = nivel
        if self.nivel == 1:
            self.background = pygame.image.load('fondo_bajo.jpg')
        if self.nivel == 2:
            self.background = pygame.image.load('fondo2.jpg')
        if self.nivel == 3:
            self.background = pygame.image.load('fondo3.jpg')

    def drawBrackground(self,screen):
        # fondo del juego
        screen.blit(self.background, (0, 0))

    def showPreviaNivel(self,screen):
        if self.nivel == 1:
            intro = True
            while intro:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    # ingresamos al juego
                    if event.type == pygame.KEYDOWN:
                        intro = False

                screen.fill((255, 255, 255))
                largeText = pygame.font.Font('space_age.ttf', 90)
                TextSurf, TextRect = text_objects("Nivel 1", largeText)
                TextRect.center = ((1200 / 2), (600 / 2))
                screen.blit(TextSurf, TextRect)
                smallText = pygame.font.Font('freesansbold.ttf', 50)
                TextSurf2, TextRect2 = text_objects("En el nivel 1 tenés que esquivar todo", smallText)
                TextRect2.center = ((1200 / 2), (600))
                screen.blit(TextSurf2, TextRect2)
                pygame.display.update()

        if self.nivel == 2:
            intro = True
            while intro:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    # ingresamos al juego
                    if event.type == pygame.KEYDOWN:
                        intro = False

                screen.fill((255, 255, 255))
                largeText = pygame.font.Font('space_age.ttf', 90)
                TextSurf, TextRect = text_objects("Nivel 2", largeText)
                TextRect.center = ((1200 / 2), (600 / 2))
                screen.blit(TextSurf, TextRect)
                smallText = pygame.font.Font('freesansbold.ttf', 50)
                TextSurf2, TextRect2 = text_objects("Ahora con tiros", smallText)
                TextRect2.center = ((1200 / 2), (600))
                screen.blit(TextSurf2, TextRect2)
                pygame.display.update()

        if self.nivel == 3:
            intro = True
            while intro:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    # ingresamos al juego
                    if event.type == pygame.KEYDOWN:
                        intro = False

                screen.fill((255, 255, 255))
                largeText = pygame.font.Font('space_age.ttf', 90)
                TextSurf, TextRect = text_objects("Nivel 3", largeText)
                TextRect.center = ((1200 / 2), (600 / 2))
                screen.blit(TextSurf, TextRect)
                smallText = pygame.font.Font('freesansbold.ttf', 50)
                TextSurf2, TextRect2 = text_objects("Tiros de todos lados", smallText)
                TextRect2.center = ((1200 / 2), (600))
                screen.blit(TextSurf2, TextRect2)
                pygame.display.update()

        if self.nivel == 4:
            intro = True
            while intro:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    # ingresamos al juego
                    if event.type == pygame.KEYDOWN:
                        pygame.quit()
                        quit()

                screen.fill((255, 255, 255))
                largeText = pygame.font.Font('space_age.ttf', 90)
                TextSurf, TextRect = text_objects("Fin del juego", largeText)
                TextRect.center = ((1200 / 2), (600 / 2))
                screen.blit(TextSurf, TextRect)
                smallText = pygame.font.Font('freesansbold.ttf', 50)
                TextSurf2, TextRect2 = text_objects("GG, you win", smallText)
                TextRect2.center = ((1200 / 2), (600))
                screen.blit(TextSurf2, TextRect2)
                pygame.display.update()