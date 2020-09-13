import pygame

class Player(object):
    def __init__(self,maxWidth,maxHeight,screen):
        self.playerImg = pygame.image.load('navejuego1.png')
        self.width = 142
        self.height = 80
        self.x = 150
        self.y = 300
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

    def setPosition(self,x,y):
        #definimos las fronteras para que el player no salga de la pantalla
        if x <= 0:
            x = 0
        if x >= (self.maxWidth - self.width):
            x = self.maxWidth - self.width
        if y <= 0:
            y = 0
        if y >= (self.maxHeight - self.height):
            y = self.maxHeight - self.height
        self.x = x
        self.y = y
    def draw(self,screen):
        screen.blit(self.playerImg,(self.x,self.y))

class Disparo(object):
    def __init__(self,Player,maxWidth,maxHeight,screen):
        self.balaImg = pygame.image.load('bala.png')
        self.width = 142
        self.height = 80
        self.balaX = Player.x + self.width
        self.balaY = Player.y + (self.height / 2)
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

    def moveBullet(self):
        self.balaX += 8

    def draw(self,screen):
        self.moveBullet()
        if self.balaX < self.maxWidth:
            screen.blit(self.balaImg,(self.balaX,self.balaY))

    def shoot(self,screen):
            screen.blit(self.balaImg,(self.balaX,self.balaY))