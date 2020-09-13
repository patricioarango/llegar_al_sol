import pygame,time

def mostrar(puntaje,nivel,segundos,screen):
    #puntaje
    posXpuntaje = 10
    posYpuntaje = 600
    font = pygame.font.Font('Roboto-Light.ttf', 32)
    score = font.render("PUNTOS: " + str(puntaje), True, (255,255,255))
    screen.blit(score,(posXpuntaje,posYpuntaje))
    #nivel
    posXnivel = 10
    posYnivel = 700
    level = font.render("Nivel: " + str(nivel) + " de 3", True, (255, 255, 255))
    screen.blit(level, (posXnivel, posYnivel))
    #tiempo
    posXreloj = 600
    posYreloj = 700
    font = pygame.font.Font('Roboto-Light.ttf', 32)
    level = font.render(time.strftime('%M:%S', time.gmtime(segundos)), True, (255, 255, 255))
    screen.blit(level, (posXreloj, posYreloj))
