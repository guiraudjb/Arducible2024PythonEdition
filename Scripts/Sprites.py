import pygame
from pygame import *


class Cible(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/Images/Boule.png")
        self.images = []
        self.images.append(pygame.image.load('./assets/Images/Boule.png'))
        self.images.append(pygame.image.load('./assets/Images/BouleG.png'))
        self.images.append(pygame.image.load('./assets/Images/BouleR.png'))
        self.rect = self.image.get_rect()
        

class Background(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load("./assets/Images/Background/0.jpg")
        self.images = []
        self.images.append(pygame.image.load('./assets/Images/Background/0.jpg'))
        self.images.append(pygame.image.load('./assets/Images/Background/1.png'))
        self.images.append(pygame.image.load('./assets/Images/Background/2.jpg'))
        self.rect = self.image.get_rect()
      
