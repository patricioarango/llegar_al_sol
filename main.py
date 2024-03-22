import pygame,math,time
import intro
import tablero
from enemigo import Roca,RocaLoca,Marciano,MarcianoPlus
from niveles import Niveles
from player import Player,Disparo

puntaje = 0
nivel_actual = 1

def main(nivel_param):
    pygame.init()

    # obtiene el número de milisegundos transcurridos después de haber llamado al método 'pygame.init()'
    start_ticks=pygame.time.get_ticks() #guardamos segundo incial

    #creamos la ventana
    maxHeight = 800
    maxWidth = 1200
    screen = pygame.display.set_mode((maxWidth,maxHeight))

    #titulo e ícono
    pygame.display.set_caption("Llegar al Sol")
    icon = pygame.image.load('favicon.ico')
    pygame.display.set_icon(icon)

    #jugador posicion inicial
    playerY_change = 0
    playerX_change = 0
    # iniciamos el jugador
    jugador = Player(maxWidth, maxHeight, screen)

    #loop presentacion
    if nivel_param == 1:
        intro.game_intro(screen)

    #lista de enemigos
    listaEnemigos = []
    def getRoca():
        listaEnemigos.append(Roca(maxWidth, maxHeight, screen))
    def getRocaLoca(cual):
        listaEnemigos.append(RocaLoca(maxWidth, maxHeight, cual,screen))
    def getMarciano():
        listaEnemigos.append(Marciano(maxWidth, maxHeight, screen))
    def getMarcianoPlus():
        listaEnemigos.append(MarcianoPlus(maxWidth, maxHeight, screen))

    listaDisparos = []

    def evaluarPuntaje():
        global puntaje
        for choque in listaEnemigos:
            #suma puntos cuando la roca desaparece de la pantalla
            if choque.x < 0 and choque.noSumoPuntos:
                choque.noSumoPuntos = False
                puntaje = puntaje + 100
                listaEnemigos.remove(choque)
            #matar a un marciano suma 500 puntos
            if isinstance(choque, Marciano):
                if choque.noExploto == 10:
                    puntaje = puntaje + 500
            #matar a un marciano plus suma 700 puntos
            if isinstance(choque, MarcianoPlus):
                if choque.noExploto == 10:
                    puntaje = puntaje + 700

    #cualquier enemigo vs jugador
    def evaluarColision():
        evaluarPuntaje()
        for enemigos in listaEnemigos:
            #calculamos que la distancia sea menor a playerWith entre nave y Rocas
            distancia = math.sqrt(math.pow(jugador.x - enemigos.x, 2) + math.pow(jugador.y - enemigos.y, 2))
            if distancia <= (jugador.width - jugador.height):
                return True

    #disparo del jugador vs enemigos Marciano OR MarcianoPlus
    def colisionDisparos():
        for enemigo in listaEnemigos:
            if isinstance(enemigo, Marciano) or isinstance(enemigo, MarcianoPlus):
                #si es un Marciano y tiene su explosion == 10 hay que eliminarlo de la lista
                if enemigo.noExploto == 10:
                    listaEnemigos.remove(enemigo)
                for disparo in listaDisparos:
                    distancia2 = math.sqrt(math.pow(disparo.balaX - enemigo.x, 2) + math.pow(disparo.balaY - enemigo.y, 2))
                    if distancia2 <= 60:
                        enemigo.noExploto = 1
                        listaDisparos.remove(disparo)

    # disparo enemigo vs player
    def colisionFuegoNoAmigo():
        for enemigo in listaEnemigos:
            if isinstance(enemigo, MarcianoPlus):
                # si es un MarcianoPlus y tiene su explosion == 10 hay que eliminarlo de la lista
                distancia3 = math.sqrt(
                        math.pow(enemigo.balaX - jugador.x, 2) + math.pow(enemigo.balaY - jugador.y, 2))
                if distancia3 <= 35:
                    gameOver(screen)

    def gameOver(screen):
        while True:
            screen.fill((255, 255, 255))
            for img in ["assets/images/gameover1.png", "assets/images/gameover2.png", "assets/images/gameover3.png", "assets/images/gameover4.png"]:
                image = pygame.image.load(img)
                screen.blit(image, (0, 0))
                pygame.display.update()
                time.sleep(0.05)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        main(nivel_param)
    #countdown
    timer_sec = 60 * 3

    timer = pygame.USEREVENT + 1
    pygame.time.set_timer(timer, 1000)  # sets timer with USEREVENT and delay in milliseconds

    nivel = Niveles(nivel_param)
    nivel.showPreviaNivel(screen)
    jugando = True
    counter = 0
    pause = False
    while jugando:
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds
        nivel.drawBrackground(screen)
        for event in pygame.event.get():
            #capturamos la X para cerrar
            if event.type == pygame.QUIT:
                jugando = False

            # agregamos pausa con la barra para debug
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = True

            if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                playerY_change = 3
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                playerY_change = -3
            #para debug ponemos un restart al pulsar R
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                main(1)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                if nivel_param == 2: #nivel 2 sólo 1 disparo por vez
                    if len(listaDisparos) == 0:
                        listaDisparos.append(Disparo(jugador,maxWidth,maxHeight,screen))
                if nivel_param == 3: #multiples disparos
                   listaDisparos.append(Disparo(jugador,maxWidth,maxHeight,screen))
            if event.type == pygame.KEYUP:
                playerY_change = 0
                playerX_change = 0

            # segun el tiempo y el nivel pedimos los enemigos
            if event.type == timer:
                if nivel_param == 2:
                    if timer_sec > 150:
                        if timer_sec % 6 == 0:
                            getRoca()
                            getMarciano()
                    if timer_sec > 120 and timer_sec < 150:
                        getRoca()
                        getMarciano()
                    if timer_sec > 90 and timer_sec < 120:
                        if timer_sec % 2 == 0:
                            getRoca()
                            getMarciano()
                    if timer_sec > 60 and timer_sec < 90:
                        getRoca()
                        getMarciano()
                    if timer_sec < 60:
                        getRoca()
                        getMarciano()
                    if timer_sec == 150:
                        getRocaLoca(1)
                        getMarciano()
                    if timer_sec == 100:
                        getRocaLoca(2)
                        getMarciano()
                    if timer_sec == 20:
                        getRocaLoca(3)
                        getMarciano()
                if nivel_param == 3:
                    if timer_sec > 150:
                        if timer_sec % 6 == 0:
                            getRoca()
                            getMarciano()
                            getMarcianoPlus()
                    if timer_sec > 120 and timer_sec < 150:
                        getRoca()
                        getMarciano()
                        getMarcianoPlus()
                    if timer_sec > 90 and timer_sec < 120:
                        if timer_sec % 2 == 0:
                            getRoca()
                            getMarciano()
                            getMarcianoPlus()
                    if timer_sec > 60 and timer_sec < 90:
                        getRoca()
                        getMarciano()
                        getMarcianoPlus()
                    if timer_sec < 60:
                        getRoca()
                        getMarciano()
                        getMarcianoPlus()
                    if timer_sec == 150:
                        getRocaLoca(1)
                        getMarciano()
                        getMarcianoPlus()
                    if timer_sec == 100:
                        getRocaLoca(2)
                        getMarciano()
                        getMarcianoPlus()
                    if timer_sec == 20:
                        getRocaLoca(3)
                        getMarciano()
                        getMarcianoPlus()
                #enemigos nivel 1
                if nivel_param == 1:
                    if timer_sec > 150:
                        if timer_sec % 6 == 0:
                            getRoca()
                    if timer_sec > 120 and timer_sec < 150:
                        getRoca()
                    if timer_sec > 90 and timer_sec < 120:
                        if timer_sec % 2 == 0:
                            getRoca()
                    if timer_sec > 60 and timer_sec < 90:
                        getRoca()
                    if timer_sec < 60:
                            getRoca()
                    if timer_sec == 150:
                        getRocaLoca(1)
                    if timer_sec == 100:
                        getRocaLoca(2)
                    if timer_sec == 20:
                        getRocaLoca(3)

                #descontamos el timer
                if timer_sec > 0:
                    timer_sec -= 1
                else:
                    if nivel_param == 1:
                        main(2)
                    if nivel_param == 2:
                        main(3)
                    if nivel_param == 3:
                        main(4)
        jugador.setPosition(jugador.x + playerX_change, jugador.y + playerY_change)
        jugador.draw(screen)

        for bala in listaDisparos:
            # si la bala no está en la pantalla la sacamos de la lista
            if bala.balaX >= maxWidth:
                listaDisparos.remove(bala)
            bala.draw(screen)

        for rival in listaEnemigos:
            rival.draw(screen)

        counter += 1
        if evaluarColision():
            gameOver(screen)

        colisionDisparos()

        colisionFuegoNoAmigo()
        #loop de pausa
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        pause = False
        tablero.mostrar(puntaje, nivel_param,timer_sec, screen)
        pygame.display.update()

main(nivel_actual)

