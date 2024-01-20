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
        self.images = []
        self.images.append(pygame.image.load('./assets/Images/Background/0.jpg'))
        self.images.append(pygame.image.load('./assets/Images/Background/1.png'))
        self.images.append(pygame.image.load('./assets/Images/Background/2.jpg'))
        self.image = self.images[0]
        self.rect = self.image.get_rect()

class ColoredRing(pygame.sprite.Sprite):
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load('./assets/Images/Background/redring.png'))
        self.images.append(pygame.image.load('./assets/Images/Background/greenring.png'))
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
 
        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.index]
 
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
       
        print(self.index)
        #finally we will update the image that will be displayed
        self.image = self.images[self.index]

 

class background_text_your_score(pygame.sprite.Sprite):
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Images/Background/high.png')
        self.rect = self.image.get_rect()

class background_text_high_score(pygame.sprite.Sprite):
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Images/Background/your.png')
        self.rect = self.image.get_rect()


class background_text_go_shooting_zone(pygame.sprite.Sprite):
    def __init__(self):
       # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/Images/Background/Go-to-the-shooting-zone.png')
        self.rect = self.image.get_rect()


