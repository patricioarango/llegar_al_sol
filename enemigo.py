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
        self.noSumoPuntos = True
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

class Marciano(object):
    def __init__(self,maxWidth,maxHeight,screen):
        self.marciImg = pygame.image.load('enemigo_2.png')
        self.boomImg = pygame.image.load('boom.png')
        self.width = 100
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.x = maxWidth - self.width
        self.height = 93
        self.y = random.randrange(maxHeight - self.height)
        self.noSumoPuntos = True
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

class MarcianoPlus(object):
    marciImg = pygame.image.load('enemigo_1.png')
    def __init__(self,maxWidth,maxHeight,screen):
        self.balaImg = pygame.image.load('balaenemiga.png')
        self.boomImg = pygame.image.load('boom.png')
        self.width = 100
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight
        self.x = maxWidth - self.width
        self.height = 80
        self.y = random.randrange(maxHeight - self.height)
        self.no_sumo_puntos = True
        self.balaX = self.x - self.width
        self.balaY = self.y + (self.height / 2) + 10
        self.noExploto = 0
        self.noSumoPuntos = True
        
    def draw(self, screen):
        self.move()
        if self.x > 0:
            if self.noExploto == 0:
                screen.blit(self.marciImg,(self.x,self.y))
            if self.noExploto > 0 and self.noExploto < 10:
                screen.blit(self.boomImg, (self.x, self.y))
                self.noExploto += 1
            self.drawBullet(screen)

    def move(self):
        self.x -= 0.8
    def moveBullet(self):
        self.balaX -= 8
    def drawBullet(self,screen):
        if self.balaX > 0:
            screen.blit(self.balaImg,(self.balaX,self.balaY))
        self.moveBullet()
    def shoot(self,screen):
            screen.blit(self.balaImg,(self.balaX,self.balaY))
