import pygame

def text_objects(text, font,color):
    textSurface = font.render(text, True, color)
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
                TextSurf, TextRect = text_objects("Nivel 1", largeText,(0,0,0))
                TextRect.center = ((1200 / 2), 100)
                screen.blit(TextSurf, TextRect)
                smallText = pygame.font.Font('freesansbold.ttf', 50)
                TextSurf2, TextRect2 = text_objects("Objetivo: tenés que esquivar todo", smallText,(0,0,0))
                TextRect2.center = ((1200 / 2), (170))
                screen.blit(TextSurf2, TextRect2)
                intro1 = pygame.image.load('intronivel1.jpg')
                screen.blit(intro1, (200, 260))
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
                TextSurf, TextRect = text_objects("Nivel 2", largeText, (0, 0, 0))
                TextRect.center = ((1200 / 2), 100)
                screen.blit(TextSurf, TextRect)
                smallText = pygame.font.Font('freesansbold.ttf', 50)
                TextSurf2, TextRect2 = text_objects("Ahora podés disparar", smallText, (0, 0, 0))
                TextRect2.center = ((1200 / 2), (170))
                screen.blit(TextSurf2, TextRect2)
                smallText = pygame.font.Font('freesansbold.ttf', 30)
                TextSurf2, TextRect2 = text_objects("(presioná la s en el teclado)", smallText, (0, 0, 0))
                TextRect2.center = ((1200 / 2), (220))
                screen.blit(TextSurf2, TextRect2)
                intro1 = pygame.image.load('intronivel2.jpg')
                screen.blit(intro1, (200, 260))
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
                TextSurf, TextRect = text_objects("Nivel 3", largeText, (0, 0, 0))
                TextRect.center = ((1200 / 2), 100)
                screen.blit(TextSurf, TextRect)
                smallText = pygame.font.Font('freesansbold.ttf', 50)
                TextSurf2, TextRect2 = text_objects("ahora te quiero ver...", smallText, (0, 0, 0))
                TextRect2.center = ((1200 / 2), (170))
                screen.blit(TextSurf2, TextRect2)
                intro1 = pygame.image.load('intronivel3.jpg')
                screen.blit(intro1, (225, 260))
                pygame.display.update()

        if self.nivel == 4:
            intro = True
            altura = 800
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
                intro1 = pygame.image.load('globos.png')
                altura = altura - 10
                if altura == -600:
                    altura = 800
                screen.blit(intro1, (0, altura))
                largeText = pygame.font.Font('space_age.ttf', 90)
                TextSurf, TextRect = text_objects("Fin del juego", largeText,(0,0,0))
                TextRect.center = ((1200 / 2), (600 / 2))
                screen.blit(TextSurf, TextRect)
                smallText = pygame.font.Font('freesansbold.ttf', 50)
                TextSurf2, TextRect2 = text_objects("GG, you win", smallText,(0,0,0))
                TextRect2.center = ((1200 / 2), (600))
                screen.blit(TextSurf2, TextRect2)
                pygame.display.update()