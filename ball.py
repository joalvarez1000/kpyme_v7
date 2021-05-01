import pygame as pg
import sys
from random import randint, choice

def rebotaX(x):
    if x <=0 or x >=ANCHO:
        return -1
    return 1
def rebotaY(y):
    if y <=0 or y >=ALTO:
        return -1
    return 1

#color bola
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)

#color pantalla
NEGRO = (0, 0, 0)

#tamaño pantalla
ANCHO = 800
ALTO = 600


pg.init()#iniciar pantalla
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock() #tiempo de desplazamiento

class Bola():
    def __init__(self, x, y, vx, vy, color): #Todas las clases de inicia con __init__ y se coloca self
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
bolas = []
for _ in range(10): #iteras 10 veces, para hacer 10 bolas
    bola = Bola(randint(0, ANCHO), #ocupas la instancia de bola()
                randint(0, ALTO),
                randint(5, 10)* choice([1, -1]),
                randint(5, 10)* choice([1, -1]),
                (randint(0, 255), randint(0,255), randint(0,255)))
    bolas.append(bola) #Se agrega el resultado de la iteración
game_over = False
while not game_over:
    v = reloj.tick(3)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
    # Modificación de estado
    for bola in bolas:
        bola.x += bola.vx
        bola.y += bola.vy
        bola.vy *= rebotaY(bola.y)
        bola.vx *= rebotaX(bola.x)
    # Gestión de la pantalla
    pantalla.fill(NEGRO)
    for bola in bolas:
        pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), 10)
    pg.display.flip()
pg.quit()
sys.exit()