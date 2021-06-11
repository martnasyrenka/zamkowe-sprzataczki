import pygame
import math
from os import path
import random

pygame.init()

#Okienko gry
screen = pygame.display.set_mode((430,460))

pygame.display.set_caption("Castle cleaners")

working_dir1 = path.dirname(__file__)

#Wczytanie grafiki protagonisty
protag_Img = pygame.image.load(path.join(working_dir1, 'protag.png')).convert()

#Wczytanie grafiki tła
background_Img = pygame.image.load(path.join(working_dir1, 'castle.jpg')).convert()

#Wstępna lokalizacja protagonisty
protagX = 180
protagY = 340
protagX_change = 0
protagY_change = 0

#Wczytanie czcionki
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32)

#Lokalizacja końcowych napisów
scoreX = 20
scoreY = 170

roomX = 200
roomY = 1

game_overX = 120
game_overY = 200

#Funkcje pojawiania się protagonisty i końcowych napisów
def protag(x,y):
    protag_Img.set_colorkey(0, 0)
    screen.blit(protag_Img,(x,y))

def show_score(x,y):
    score = font.render("You've cleaned the room!", True, (0,0,0))
    screen.blit(score, (x,y))

def collisionTrue(protagX,protagY,roomX,roomY):
    distance = math.sqrt((math.pow(roomX-protagX,2)) + (math.pow(roomY-protagY,2)))
    if distance < 25:
        return True
    else:
        return False

def show_game_over(x,y):
    game_over = font.render("GAME OVER", True, (0,0,0))
    screen.blit(game_over, (x,y))
    
#Klasa bałaganu do posprzątania pojawiającego się na mapie gry
class Trash(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(path.join(working_dir1, 'trash.png')).convert()
        self.image.set_colorkey(0, 0)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,pos_y]

trash_group = pygame.sprite.Group()
for trash in range(5):
    new_trash = Trash(random.randrange(50,400),random.randrange(50,400))
    trash_group.add(new_trash)
    
#Klasa miotły (gracza/myszki)
class Broom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(path.join(working_dir1, 'broom.png')).convert()
        transColor = (255,255,255)
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.clean = pygame.mixer.Sound(path.join(working_dir1, 'cleaning_sound.wav'))

    def cleaning(self):
        self.clean.play()
        pygame.sprite.spritecollide(broom,trash_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

broom = Broom()
broom_group = pygame.sprite.Group()
broom_group.add(broom)

pygame.mouse.set_visible(False)

#Pętla gry
running = True
while running:
    
    screen.blit(background_Img,(0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #Poruszanie się gracza za pomoca strzałek
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                protagX_change = -10
                if collision:
                    protagX_change = 0
            if event.key == pygame.K_RIGHT:
                protagX_change = 10
                if collision:
                    protagX_change = 0
            if event.key == pygame.K_UP:
                protagY_change = -10
                if collision:
                    protagY_change = 0
            if event.key == pygame.K_DOWN:
                protagY_change = 10
                if collision:
                    protagY_change = 0
        if event.type == pygame.KEYUP:
            if event.type == pygame.KEYDOWN or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                protagX_change = 0
                protagY_change = 0
                
        #Sprzątanie za pomocą kliknięcia myszki
        if event.type == pygame.MOUSEBUTTONDOWN:
            broom.cleaning()

        protagX += protagX_change
        protagY += protagY_change
        
        #Ściany gry
        if protagX <= 0:
            protagX = 0
        elif protagX >= 365:
            protagX = 365

        if protagY <= 0:
            protagY = 0
        elif protagY >= 355:
            protagY = 355

    #Kolizja protagonisty z metą (koniec zamku) i pojawienie się napisów
    collision = collisionTrue(protagX,protagY,roomX,roomY)
    if collision:
        show_score(scoreX,scoreY)
        show_game_over(game_overX,game_overY)
    
    #Aktywacja bałaganu/protagonisty etc.
    trash_group.draw(screen)
    broom_group.draw(screen)
    broom_group.update()
    protag(protagX,protagY)

    pygame.display.update()
