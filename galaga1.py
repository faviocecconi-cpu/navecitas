from pygame import *


#música de fondo
mixer.init()
mixer.music.load('fire.ogg')
mixer.music.play()
fire_sound = mixer.Sound('fire.ogg')


#necesitamos las siguientes imágenes:
img_back = "galaxy.jpg" #fondo de juego
img_hero = "rocket.png" #héroe


#clase padre para otros objetos
class GameSprite(sprite.Sprite):
 #constructor de clase
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #Llamada al constructor de la clase (Sprite):
       sprite.Sprite.__init__(self)


       #cada objeto debe almacenar la propiedad image
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed

       #cada objeto debe tener la propiedad rect – el rectángulo en el que está
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 #método de dibujo del personaje en la ventana
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))


#clase de jugador principal
class Player(GameSprite):
   #método para controlar el objeto con las teclas de las flechas
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
 #método para “disparar” (usa la posición del jugador para crear una bala)
   def fire(self):
       pass


#Crea una ventana
win_width = 700
win_height = 500
display.set_caption("Tirador")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


#crea objetos
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)


#la variable “el juego terminó”: cuando sea True, los objetos dejan de funcionar en el ciclo principal
finish = False
#Ciclo de juego principal:
run = True #la bandera se restablece por el botón de cerrar ventana
while run:
   #Evento de pulsado del botón “Cerrar”
   for e in event.get():
       if e.type == QUIT:
           run = False


   if not finish:
       #actualiza el fondo
       window.blit(background,(0,0))


       #ejecuta los movimientos del objeto
       ship.update()


       #los actualiza en una nueva ubicación en cada iteración del ciclo
       ship.reset()


       display.update()
   #el ciclo se ejecuta cada 0.05 seg
   time.delay(50)
