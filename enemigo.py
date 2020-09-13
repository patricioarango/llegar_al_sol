import pygame,random,math

class Roca(object):
    #roca
    rocaImg = pygame.image.load('roca.png')
    def __init__(self,maxWidth,maxHeight,screen):
        self.width = 64
        self.x = maxWidth - self.width
        self.height = 64
        self.y = random.randrange(maxHeight - self.height)
        self.noSumoPuntos = True
    def draw(self, screen):
        self.move()
        if self.x > 0:
            screen.blit(self.rocaImg,(self.x,self.y))
    def move(self):
        self.x -= 1

class RocaLoca(object):
    #roca
    rocaImg = pygame.image.load('roca.png')
    def __init__(self,maxWidth,maxHeight,cual,screen):
        self.cual = cual
        self.width = 64
        self.x = maxWidth - self.width
        self.height = 64
        self.y = random.randrange(maxHeight - self.height)
        self.no_sumo_puntos = True
        # self.path = [x, end]  # This will define where our enemy starts and finishes their path.
        # self.walkCount = 0
        # self.vel = 3
    def draw(self, screen):
        self.move()
        if self.x > 0:
            screen.blit(self.rocaImg,(self.x,self.y))
        return self.x,self.y
    def move(self):
        self.x -= 0.8
        #1
        if self.cual == 1:
            y = (math.sin(self.x / 50) * 100) + (300)
        #2
        if self.cual == 2:
            y = (math.sin(self.x / 25) * 100) + 250
        # 3
        if self.cual == 3:
            y = (math.sin(self.x / 90) * (600 - 64))

        if y < 0:
            y = math.ceil(y * -1)

        self.y = y

    def setNoSumoPuntos(self):
        self.no_sumo_puntos = False
    def getNoSumoPuntos(self):
        return self.no_sumo_puntos
    def getPosicion(self):
        return [self.x,self.y]

class Marciano(object):
    def __init__(self,maxWidth,maxHeight,screen):
        self.marciImg = pygame.image.load('sol2.png')
        self.boomImg = pygame.image.load('boom.png')
        self.width = 85
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.x = maxWidth - self.width
        self.height = 113
        self.y = random.randrange(maxHeight - self.height)
        self.no_sumo_puntos = True
        self.noExploto = 0
        # self.path = [x, end]  # This will define where our enemy starts and finishes their path.
        # self.walkCount = 0
        # self.vel = 3
    def draw(self, screen):
        self.move()
        if self.x > 0:
            if self.noExploto == 0:
                screen.blit(self.marciImg,(self.x,self.y))
            if self.noExploto > 0 and self.noExploto < 10:
                screen.blit(self.boomImg, (self.x, self.y))
                self.noExploto += 1

    def move(self):
        self.x -= 0.8
    def setNoSumoPuntos(self):
        self.no_sumo_puntos = False
    def getNoSumoPuntos(self):
        return self.no_sumo_puntos

class MarcianoPlus(object):
    marciImg = pygame.image.load('sol_3.png')
    def __init__(self,maxWidth,maxHeight,screen):
        self.width = 85
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.x = maxWidth - self.width
        self.height = 113
        self.y = random.randrange(maxHeight - self.height)
        self.no_sumo_puntos = True
        # self.path = [x, end]  # This will define where our enemy starts and finishes their path.
        # self.walkCount = 0
        # self.vel = 3
    def draw(self, screen):
        self.move()
        if self.x > 0:
            screen.blit(self.marciImg,(self.x,self.y))

    def move(self):
        self.x -= 0.8
    def setNoSumoPuntos(self):
        self.no_sumo_puntos = False
    def getNoSumoPuntos(self):
        return self.no_sumo_puntos