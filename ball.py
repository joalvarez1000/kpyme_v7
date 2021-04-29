import pygame as pg
import sys

#color de la bola 
ROJO  = (255, 0, 0)
AZUL  = (0, 0, 255)
VERDE = (0, 255, 0)

#tamaño de la pantalla

ANCHO = 800
ALTO = 600

#Color de la pantalla
NEGRO = (0,0,0)

#Coordenadas para la bola
x = ANCHO //2
y = ALTO //2

#Velocidades de la bola 
vx = -7
vy = -7
#crear pantalla
pg.init()
pantalla = pg.display.set_mode((ANCHO,ALTO))

#fps de la bola
reloj = pg.time.Clock()

game_over = False

while not game_over:
    #inicializar el fps de la bola 
    reloj.tick (60)

    #gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True

    #Modificacion de estado
    x += vx
    y += vy

    #bola choca con las paredes

        #refactorizacion del codigo
        #if y >= 0:
        #    vy = -vy
        #elif y <= ALTO:
        #    vy = -vy
    if y <= 0 or y >= ALTO:
        vy = -vy

        #if x <= 0:
        #    vx = -vx
        #elif x >= ANCHO:
        #    vx = -vx
    if x <= 0 or x >= ANCHO:
        vx = -vx

    #Gestion de la pantalla
    pantalla.fill(NEGRO)
    #dibujar la bola (lasuperficie, colordelabola ,elcentro.lamitad.de.lapantalla, radiobola)
    pg.draw.circle(pantalla, ROJO,  (x, y), 10)
    
       
    #refrescar pantalla
    pg.display.flip()

pg.quit()
sys.exit()
