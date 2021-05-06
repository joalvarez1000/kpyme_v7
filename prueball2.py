import pygame as pg
import sys

ANCHO = 800
ALTO = 600
NEGRO = (0 , 0, 0)
ROJO = (255, 0, 0)

pg.init()

pantalla = pg.display.set_mode ((ANCHO, ALTO))

game_over = False

while not game_over:
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
    
    pantalla.fill (NEGRO)
    pg.draw.circle (pantalla, ROJO, (ANCHO//2, ALTO//2), 10)
    

    pg.display.flip()

pg.quit()
sys.exit()
    