import pygame
from pygame import *
pygame.init()
from Scripts.init import * # load config.ini and some variables
from Scripts.Sprites import Cible,Background,BackgroudFrame,background_text_your_score,background_text_high_score,background_text_go_shooting_zone,ColoredRing# load sprites

def init_game():
    global cible1
    global cible2
    global cible3
    cible1 = Cible()
    cible1.image = pygame.transform.scale(cible1.image, (384, 384))
    cible1.rect.x = 188
    cible1.rect.y = 600

    cible2 = Cible()
    cible2.image = pygame.transform.scale(cible2.image, (384, 384))
    cible2.rect.x = 768
    cible2.rect.y = 600

    cible3 = Cible()
    cible3.image = cible3.images[1]
    cible3.image = pygame.transform.scale(cible3.image, (384, 384))
    cible3.rect.x = 1348
    cible3.rect.y = 600
    
    ending_screen_text_high.rect.x = 478
    ending_screen_text_high.rect.y = 110    
    
    ending_screen_text_your.rect.x = 478
    ending_screen_text_your.rect.y = 650
    
    adervtising_shooting_zone.rect.x = 448
    adervtising_shooting_zone.rect.y = 708
    



def next_gamestate():
    global time_left
    global gamestate
    global score
    global intro_length
    global game_length
    global ending_length
    global ingamebackground
    if gamestate == 0:
        gamestate = 1
        ingamebackground.image = ingamebackground.images[0]
        time_left = game_length
        score = 0
    elif gamestate == 1:
        gamestate = 2
        ingamebackground.image = ingamebackground.images[2]
        time_left = ending_length
    elif gamestate == 2:
        gamestate = 0
        time_left = intro_length
        pygame.mixer.music.load('./assets/Sounds/VoicesAI/readytogo.wav')
        pygame.mixer.music.play(1)

def ciblealeatoire():
    global cibleencours
    global oldcibleencours
    while cibleencours == oldcibleencours:
        cibleencours = random.randint(1, 3)
    oldcibleencours = cibleencours 

def showcam():
    mycam.rect.x = mycam.rect.x + Decalagex
    ecran.blit(mycam.images, mycam.rect)
   
    #if mycam.zoneinterdite:
    #    draw_ellipse_angle(ecran, (255, 0, 0), (848, 0, mycam.LargeurChampCamera, 384), 0, 5)
    #else:
    #    draw_ellipse_angle(ecran, (0, 255, 0), (848, 0, mycam.LargeurChampCamera, 384), 0, 5)
        
def countdown():
    global old_timer
    global game_timer
    global time_left
    game_timer = pygame.time.get_ticks()
    if game_timer - old_timer >= 1000:
        time_left = time_left - 1
        old_timer = game_timer

def update_score():
    global score
    global time_left
    if sound_effects == True:
        pygame.mixer.music.load('./assets/Sounds/Son3.wav')
        pygame.mixer.music.play(1)
    
    score = score + 1
    time_left = time_left + 5

def draw_ellipse_angle(surface, color, rect, angle, width=0):
    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))
    

#initialise background table
introbackground = BackgroudFrame()
ingamebackground = Background()
camring = ColoredRing()
ending_screen_text_your = background_text_your_score()
ending_screen_text_high = background_text_high_score()
adervtising_shooting_zone = background_text_go_shooting_zone()

#initialise webcam if actived in config.ini
if active_webcam:
    try:
        from Scripts.opencvcam import Cam
        mycam = Cam()
        if mycam.webcam_compatibility == True:
            webcam_compatibility = True
        else:
            webcam_compatibility = False
            
        if webcam_compatibility == True:
            
            print("ok")
            Decalagex = (LARGEUR_ECRAN - mycam.LargeurChampCamera) / 2 
            ingamebackground.images[1] = pygame.image.load('./assets/Images/Background/1.png')
        else:
            webcam_zone_interdite = False
            ingamebackground.images[1] = pygame.image.load('./assets/Images/Background/1.jpg')
    except:
        print("cam unsuported. CPU is too old")
        webcam_compatibility = False
        webcam_zone_interdite = False
        ingamebackground.images[1] = pygame.image.load('./assets/Images/Background/1.jpg')
        
else:
    webcam_compatibility = False
    webcam_zone_interdite = False
    ingamebackground.images[1] = pygame.image.load('./assets/Images/Background/1.jpg')

# run the background game music
if background_music == True:
    music = pygame.mixer.Sound('./assets/Sounds/guardians.mp3')
    channel1 = pygame.mixer.Channel(0)
    channel1.play(music, loops = -1)
    
    


    #pygame.mixer.Channel(0).play(pygame.mixer.Sound('./assets/Sounds/guardians.mp3'))
    #pygame.mixer.Channel(0).stop_here

#initialise the screen
pygame.display.set_caption("Arducible PÉTANQUE GAME") # set window title
if Fullscreen:
    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN), pygame.SCALED | pygame.FULLSCREEN, vsync=1)
else:
    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN), pygame.SCALED )



init_game()
#main game loop
while continuer:
    if gamestate == 0:
        countdown()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    continuer = False
            elif event.type == pygame.KEYUP:
                #press m key to mute/unmute only backgroud music
                if event.key == pygame.K_m:
                        if channel1.get_busy():
                            channel1.fadeout(FadeoutTime)
                        else:
                            channel1.play(music, loops = -1)
                #press s key to mute/unmute soud effects and music
                if event.key == pygame.K_s:
                    if sound_effects == True:
                        if channel1.get_busy():
                            channel1.fadeout(FadeoutTime)
                        sound_effects = False
                    else:
                        sound_effects = True
                        #if not channel1.get_busy():
                        channel1.play(music, loops = -1)
                    
                        
                        
        
        introbackground.update()
        ecran.blit(introbackground.image, introbackground.rect)

        Time_left_image = FONT.render( "Time left  : " + str(time_left), True, (66, 236, 255))
        Time_left_image_mask = GAME_FONT.render( "Time left  : " + str(time_left), True, (12, 152, 192))
        ecran.blit(Time_left_image,(10,10))
        ecran.blit(Time_left_image_mask,(11,10))
        
        High_score_image = FONT.render("High score : " + str(high_score), True, (66, 236, 255))
        ecran.blit(High_score_image, (10,202))
        
             
        pygame.display.flip()
        if time_left <= 0:
            next_gamestate()
        
    
    if gamestate == 1:
        countdown()
        
        
        if webcam_compatibility == True:
            mycam.update(mycam.cap, mycam.mp_drawing,mycam.mp_pose, mycam.LimiteBasseCamera, mycam.LimiteHauteCamera, mycam.LimiteGaucheCamera, mycam.LimiteDroiteCamera)
            webcam_zone_interdite = mycam.zoneinterdite
            showcam()
            ecran.blit(ingamebackground.image, ingamebackground.rect)

            if mycam.zoneinterdite == True:
                #Info_image = FONT.render("Go to the shooting zone !!!", True, (255, 0, 0))
                #Info_image_rect = Info_image.get_rect()
                #ecran.blit(Info_image,(LARGEUR_ECRAN/2-Info_image_rect.right/2, 492))
                camring.image = camring.images[0]
                ecran.blit(camring.image, (831,0))
            else:
                camring.image = camring.images[1]
                ecran.blit(camring.image, (831,0))
        else:
            ecran.blit(ingamebackground.image, ingamebackground.rect)
        
        
        for event in pygame.event.get():
            
            
            if event.type == pygame.QUIT:
                
                continuer = False
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    continuer = False
                
          
            elif event.type == pygame.KEYUP:
                
                if webcam_zone_interdite == False:
                    
                    if event.key == pygame.K_e:
                        
                        if cibleencours == 1:
                            update_score()
                            ciblealeatoire()
                    
                    if event.key == pygame.K_r:
                        
                        if cibleencours == 2:
                            update_score()
                            ciblealeatoire() 
                    
                    if event.key == pygame.K_t:
                        
                        if cibleencours == 3:
                            update_score()
                            ciblealeatoire()
                    
                    if event.key == pygame.K_m:
                        if channel1.get_busy():
                            channel1.fadeout(FadeoutTime)
                        else:
                            channel1.play(music, loops = -1)
                    
                    if event.key == pygame.K_s:
                        if sound_effects == True:
                            if channel1.get_busy():
                                channel1.fadeout(FadeoutTime)
                                sound_effects = False
                        else:
                            sound_effects = True
                            #if not channel1.get_busy():
                            channel1.play(music, loops = -1)

                
                    
        if level > oldlevel or level < oldlevel:
            ingamebackground.image = ingamebackground.images[level]
            oldlevel=level

        if cibleencours == 1:
            
            cible1.image = cible1.images[1]
            cible2.image = cible1.images[0]
            cible3.image = cible1.images[0]
        
        elif cibleencours == 2:
            
            cible1.image = cible1.images[0]
            cible2.image = cible1.images[1]
            cible3.image = cible1.images[0]
        
        elif cibleencours == 3:
            
            cible1.image = cible1.images[0]
            cible2.image = cible1.images[0]
            cible3.image = cible1.images[1]
        
        cible1.image = pygame.transform.scale(cible1.image, (384, 384))
        cible2.image = pygame.transform.scale(cible2.image, (384, 384))
        cible3.image = pygame.transform.scale(cible3.image, (384, 384))
        ecran.blit(cible1.image, cible1.rect)
        ecran.blit(cible2.image, cible2.rect)
        ecran.blit(cible3.image, cible3.rect)
        if mycam.zoneinterdite == True:
            ecran.blit(adervtising_shooting_zone.image, adervtising_shooting_zone.rect)
        #Time_left_image = FONT.render("Time left : " + str(time_left), True, (66, 236, 255))
        #ecran.blit(Time_left_image,(10,10))
        
        if time_left <= 15:
            Arcade_center_image = Arcade_Font.render(str(time_left), True, (255, 0, 0))
        elif time_left <= 30:
            Arcade_center_image = Arcade_Font.render(str(time_left), True, (255, 128, 0))
        elif time_left <= 45:
            Arcade_center_image = Arcade_Font.render(str(time_left), True, (255, 255, 0))
        elif time_left >= 60:
            Arcade_center_image = Arcade_Font.render(str(time_left), True, (255, 233, 0))
        else:
            Arcade_center_image = Arcade_Font.render(str(time_left), True, (0, 255, 0))



        #define time left position and blit
        if len(str(time_left)) == 1:
            ecran.blit(Arcade_center_image,(894,400))
        if len(str(time_left)) == 2:
            ecran.blit(Arcade_center_image,(794,400))        
        if len(str(time_left)) == 3:
            ecran.blit(Arcade_center_image,(696,400))
                  
        Score_image = FONT.render("Score     : " + str(score), True, (66, 236, 255))
        ecran.blit(Score_image,(10,106))

        pygame.display.flip()
        
        if time_left <= 0:
            next_gamestate()
        clock.tick(60)
        
    if gamestate == 2:
        
        countdown()
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
            
                continuer = False
            
            elif event.type == pygame.KEYDOWN:
            
                if event.key == pygame.K_ESCAPE:
            
                    continuer = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_m:
                        if channel1.get_busy():
                            channel1.fadeout(FadeoutTime)
                        else:
                            channel1.play(music, loops = -1)
                            
                if event.key == pygame.K_s:
                    if sound_effects == True:
                        if channel1.get_busy():
                            channel1.fadeout(FadeoutTime)
                        sound_effects = False
                    else:
                        sound_effects = True
                        #if not channel1.get_busy():
                        channel1.play(music, loops = -1)
                
        
        if score >= high_score:
            
            high_score = score
        
        ecran.blit(ingamebackground.image, ingamebackground.rect)
        Time_left_image = FONT.render("Time left  : " + str(time_left), True, (66, 236, 255))
        ecran.blit(Time_left_image,(10,10))
        
        ecran.blit(ending_screen_text_high.image, ending_screen_text_high.rect)
        High_score_image = Arcade_Font.render(str(high_score), True, (66, 236, 255))
        ecran.blit(High_score_image, (892,810))
        
        ecran.blit(ending_screen_text_your.image, ending_screen_text_your.rect)
        Score_image = Arcade_Font.render(str(score), True, (66, 236, 255))
        ecran.blit(Score_image,(892,270))

        pygame.display.flip()
        
        if time_left <= 0:
            next_gamestate()

    clock.tick(30)


pygame.quit
