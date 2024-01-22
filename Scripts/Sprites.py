import pygame
from pygame import *
from Scripts.init import *


class Cible(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('./assets/Images/Boule.png'))
        self.images.append(pygame.image.load('./assets/Images/BouleG.png'))
        self.images.append(pygame.image.load('./assets/Images/BouleR.png'))
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (LARGEUR_ECRAN*0.2, HAUTEUR_ECRAN*0.35))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        
        #cible1.image = pygame.transform.scale(pygame.image.load('./assets/Images/BouleG.png'), (LARGEUR_ECRAN*0.2, HAUTEUR_ECRAN*0.35))
        

class Background(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('./assets/Images/Background/1.jpg'))
        self.images.append(pygame.image.load('./assets/Images/Background/1.png'))
        self.images.append(pygame.image.load('./assets/Images/Background/2.jpg'))
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (LARGEUR_ECRAN, HAUTEUR_ECRAN))
        self.image = self.images[0]
        self.rect = self.image.get_rect()

class ColoredRing(pygame.sprite.Sprite):
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('./assets/Images/Background/redring.png'))
        self.images.append(pygame.image.load('./assets/Images/Background/greenring.png'))
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (258 * LARGEUR_ECRAN/1920, 395 * HAUTEUR_ECRAN/1080))
        self.image = self.images[0]
        self.rect = self.image.get_rect()
 
class BackgroudFrame(pygame.sprite.Sprite):
    
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
     
        self.images = []
        self.images.append(pygame.image.load('./assets/Images/frame/1.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/2.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/3.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/4.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/5.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/6.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/7.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/8.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/9.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/10.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/11.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/12.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/13.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/14.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/15.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/16.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/17.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/18.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/19.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/20.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/21.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/22.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/23.png'))
        self.images.append(pygame.image.load('./assets/Images/frame/24.png'))
        self.index = 0
        for i in range(len(self.images)):
            self.images[i] = pygame.transform.scale(self.images[i], (LARGEUR_ECRAN, HAUTEUR_ECRAN))
 
        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.index]
        print(HAUTEUR_ECRAN)
 
        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = self.image.get_rect()
        self.increaseindex = True
    def update(self):
        #when the update method is called, we will increment the index
        if self.index >= len(self.images) - 1:
            #descrease
            self.increaseindex = False
        
        if self.index <= 0:
            self.increaseindex = True
        
        if self.increaseindex == True:
            self.index += 1
            
        else:
            self.index -= 1
       
        #print(self.index)
        #finally we will update the image that will be displayed
        self.image = self.images[self.index]


