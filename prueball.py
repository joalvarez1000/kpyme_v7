import pygame as pg
import sys
import random

ANCHO = 800
ALTO = 600
FPS = 60

class Marcador ():
    def __init__ (self, x, y, fontsize = 25, color = (255,255,255),):
        self.fuente = pg.font.SysFont("Arial", fontsize)
        self.x = x
        self.y = y
        self.color = color
    def dibuja (self, text, lienzo):
        image = self.fuente.render(str (text), True, self.color)
        lienzo.blit (image, (self.x, self.y))

class Bola(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self) #estoy inicializando de sprite
        # super().__init__()  -> segunda forma de inicializar
        self.image = pg.image.load ('./Images/ball1.png').convert_alpha()#instancia de surface
        self.rect = self.image.get_rect(center=(x,y)) #instancia de rect
        
        self.vx = random.randint(5, 10)*random.choice([-1, 1])
        self.vy = random.randint(5, 10)*random.choice([-1, 1])

    def update (self): #actualizar para que se mueva la bola
        self.rect.x += self.vx
        self.rect.y += self.vy    

        if self.rect.left <= 0 or self.rect.right >= ANCHO:
            self.vx *=-1
        if self.rect.top <= 0 or self.rect.bottom >= ALTO:
            self.vy *=-1

class Game():
    def __init__(self):
        self.pantalla = pg.display.set_mode ((ANCHO, ALTO)) #creamos la pantalla
        self.botes = 0 # puntuacion
        self.cuentaGolpes = Marcador (10,10)

        self.ballGroup = pg.sprite.Group()
        for i in range(random.randint(1,20)):
            bola = Bola (random.randint(0, ANCHO), random.randint(0,ALTO))
            self.ballGroup.add(bola)# inicializamos la bola de la Class Bola con el grupo

           
    def bucle_principal (self):
        game_over = False
        reloj = pg.time.Clock()
        while not game_over:
            reloj.tick(FPS)

            #GESTION DE EVENTOS

            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    game_over = True
            
            self.ballGroup.update()
            
            self.pantalla.fill((0,0,0))
            self.cuentaGolpes.dibuja("Hola", self.pantalla)
            self.ballGroup.draw(self.pantalla)

            pg.display.flip()

if __name__ == '__main__':
    pg.init()
    game = Game()
    game.bucle_principal()