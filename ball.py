import pygame as pg
import sys
from random import randint, choice

ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
NEGRO = (0, 0, 0)
BLANCO = (255,255,255)
ANCHO = 800
ALTO = 600
pg.init()
pantalla = pg.display.set_mode((ANCHO, ALTO))
reloj = pg.time.Clock()


class Bola():
    
    # si pongo aqui radio (radio = 10) variable de clase o atributos estaticos
    def __init__(self, x, y, vx=5, vy=5, color= (255, 255, 255), radio=10):
        self.x = x # estas se llaman variable de instancia
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.anchura = radio*2
        self.altura = radio*2
    def actualizar(self):
        self.x += self.vx
        self.y += self.vy
        if self.y <=0: #evitamos que la bola se salga del marco
            self.vy = -self.vy
        if self.x <=0 or self.x >=ANCHO:
            self.vx = -self.vx
        if self.y >=ALTO:
            self.x = ANCHO //2
            self.y = ALTO //2
            self.vx = randint (5, 10)*choice([-1, 1])
            self.vy = randint (5, 10)*choice([-1, 1])
            pg.time.delay(1000)
            return True
        return False
    '''
        bola.dibujar(pantalla)
        #pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), 10)
    '''
    def dibujar(self, lienzo):
        pg.draw.circle(lienzo, self.color, (self.x, self.y), self.anchura//2)
    
    def comprueba_colision (self, objeto):
        # comprueba si chocan en la interseccion de las x & la y
        choqueX= self.x >= objeto.x and self.x <= objeto.x + objeto.anchura or \
            self.x +self.anchura >= objeto.x and self.x + self.anchura <= objeto.x + objeto.anchura
        choqueY= self.y >= objeto.y and self.y <= objeto.y + objeto.altura or \
            self.y +self.altura >= objeto.y and self.y + self.altura <= objeto.y + objeto.altura
        
        if choqueX and choqueY:
            self.vy *= -1
            return True
        return False

class Raqueta(): # vamos a acrear una raqueta
    def __init__ (self, x=0, y=0):
        self.altura = 10
        self.anchura = 100
        self.color = (255,255,255)
        self.x = (ANCHO + self.anchura) // 2
        self.y = ALTO - self.altura - 15
        self.vy = 0 #no se mueve por la vertical
        self.vx = 13 #se mueve por la horizontal de la pantalla
    
    def dibujar (self, lienzo):
        rect = pg.Rect(self.x, self.y, self.anchura, self.altura) #creamos un rectangulo en una variable
        pg.draw.rect(lienzo, self.color, rect) # dibujamos el rectangulo, y lo incluimos en el draw
    
    def actualizar (self):
        teclas_pulsadas = pg.key.get_pressed() #me devuelve la tecla que esta pulsada
        if teclas_pulsadas [pg.K_LEFT] and self.x> 0:
            self.x -= self.vx
        if teclas_pulsadas [pg.K_RIGHT] and self.x < ANCHO - self.anchura:
            self.x += self.vx

vidas = 3    
puntuacion  = 0
bola = Bola(randint(0, ANCHO), # solo dejamos  una bola 
            randint(0, ALTO),
            randint(5, 10)*choice([-1, 1]),
            randint(5, 10)*choice([-1, 1]),
            (randint(0, 255), randint(0,255), randint(0,255)))
    
raqueta = Raqueta()

txtGameOver = pg.font.SysFont ("Arial", 35)
txtPuntuacion = pg.font.SysFont ("Courrier", 28)
pierdebola =False
game_over = False
while not game_over and vidas > 0:
    v = reloj.tick(60)
    if pierdebola:
        pg.time.delay(500)
    #Gestion de eventos
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game_over = True
        
            
    # Modificación de estado
    raqueta.actualizar()
    pierdebola = bola.actualizar() #solo actualizamos una bola
    pantalla.fill(NEGRO) #limpio la pantalla
    if pierdebola:
        vidas -= 1
        #resetear la bola
        if vidas == 0:
            texto = txtGameOver.render("GAME_OVER", True, (0, 255, 255)) #renderizo el texto
            pantalla.blit(texto, (400, 300)) # lo guardo en memoria
        else:
            bola.x =400
            bola.y =300
            bola.dibujar(pantalla)
            raqueta.dibujar(pantalla)
    else:
        if bola.comprueba_colision(raqueta):
            puntuacion +=5


        # Gestión de la pantalla
        texto = txtPuntuacion.render (str(puntuacion), True, (255,255,0))
        pantalla.blit(texto, (20, 20))
        bola.dibujar(pantalla) #dibujamo con la instancia creada en la clase bola()
        raqueta.dibujar (pantalla)
        #pg.draw.circle(pantalla, bola.color, (bola.x, bola.y), 10)
    pg.display.flip()#refresca la pantalla
   
        
pg.time.delay(1000)
pg.quit()
sys.exit()