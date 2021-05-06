import pygame as pg
import sys

NEGRO = (0,0,0)
ROJO = (255,0,0)
ANCHO = 800
ALTO = 600
pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()


x = ANCHO //2
y = ALTO  // 2
vx = -5
vy = -5

game_over = False
while not game_over:
    v = reloj.tick (60)
    for evento in pg.event.get ():
        if evento.type == pg.QUIT:
            game_over = True
    
    x += vx
    y += vy 

    if x <= 0 and x >= ANCHO:
        vx -= vx
    if y <= 0 and y >= ALTO:
        vy -= vy

    pantalla.fill(NEGRO)
    pg.draw.circle(pantalla, ROJO, (x, y), 10) 

    pg.display.flip()

pg.exit()
sys.exit()
    
    