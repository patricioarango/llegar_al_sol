import pygame, random,math
import intro
import tablero
from enemigo import Roca,RocaLoca,Marciano
from niveles import Niveles
from player import Player,Disparo

# puntaje
puntaje = 0
# nivel
nivel_actual = 3

def main(nivel_param):
    # inicializamos el juego
    pygame.init()

    # obtiene el número de milisegundos transcurridos después de haber llamado al método 'pygame.init()'
    start_ticks=pygame.time.get_ticks() #guardamos segundo incial

    #creamos la ventana
    maxHeight = 600
    maxWidth = 1200
    #la ventana tiene 200px más de alto por el tablero
    screen = pygame.display.set_mode((maxWidth,800))

    #titulo e ícono
    pygame.display.set_caption("Llegar el Sol")
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

    def evaluarColision():
        evaluarPuntaje()
        for enemigos in listaEnemigos:
            #calculamos que la distancia sea menor a playerWith entre nave y Rocas
            distancia = math.sqrt(math.pow(jugador.x - enemigos.x, 2) + math.pow(jugador.y - enemigos.y, 2))
            if distancia <= (jugador.width - jugador.height):
                return True

    def colisionDisparos():
        for enemigo in listaEnemigos:
            if isinstance(enemigo, Marciano):
                #si es un Marciano y tiene su explosion mayor a 5 hay que eliminarlo de la lista
                if enemigo.noExploto == 10:
                    listaEnemigos.remove(enemigo)
                for disparo in listaDisparos:
                    distancia2 = math.sqrt(math.pow(disparo.balaX - enemigo.x, 2) + math.pow(disparo.balaY - enemigo.y, 2))
                    if distancia2 <= 60:
                        enemigo.noExploto = 1
                        listaDisparos.remove(disparo)


    #countdown
    #timer_sec = 60 * 3
    timer_sec = 20
    # USEREVENTS are just integers
    # you can only have like 31 of them or something arbitrarily low
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
            #sin movernos la nave empieza a bajar
            #playerY_change = +1
            # capturamos movimiento de la barra espaciadora
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pause = True
                #playerY_change = -4
                #playerX_change = 0.2
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
                if nivel_param == 2:
                    listaDisparos.append(Disparo(jugador,maxWidth,maxHeight,screen))
            if event.type == pygame.KEYUP:
                playerY_change = 0
                playerX_change = 0

            # segun el tiempo y el nivel pedimos los enemigos
            if event.type == timer:
                #enemigos nivel 2
                if nivel_param == 2:
                    getMarciano()
                    if timer_sec == 20:
                        getMarciano()
                    if timer_sec > 90 and timer_sec < 120:
                        if timer_sec % 2 == 0:
                            getRoca()
                            #getMarciano()
                    if timer_sec < 60:
                        getRoca()
                        #getMarciano()
                    if timer_sec == 150:
                        getRocaLoca(1)
                    if timer_sec == 100:
                        getRocaLoca(2)
                    if timer_sec == 20:
                        getRocaLoca(3)

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
            bala.draw(screen)

        for rock in listaEnemigos:
            rock.draw(screen)

        counter += 1
        if evaluarColision():
            intro.gameOver(screen)

        colisionDisparos()
        #loop de pausa
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        pause = False
        tablero.mostrar(puntaje, nivel_param,timer_sec, screen)
        pygame.display.update()

main(nivel_actual)

