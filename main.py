import pygame
from pygame import *
pygame.init()
from Scripts.init import * # load config.ini and some variables
from Scripts.Sprites import *# load sprites

def init_game():
    global cible1
    global cible2
    global cible3
    cible1 = Cible()
    cible1.image = pygame.transform.scale(cible1.image, (384, 384))
    cible1.rect.x = 188
    cible1.rect.y = 700

    cible2 = Cible()
    cible2.image = pygame.transform.scale(cible2.image, (384, 384))
    cible2.rect.x = 768
    cible2.rect.y = 700

    cible3 = Cible()
    cible3.image = cible3.images[1]
    cible3.image = pygame.transform.scale(cible3.image, (384, 384))
    cible3.rect.x = 1348
    cible3.rect.y = 700
    
def next_gamestate():
    global time_left
    global gamestate
    global score
    global intro_length
    global game_length
    global ending_length
    global ingamebackground
    global webcam_compatibility
    if gamestate == 0:
        gamestate = 1
        if webcam_compatibility == True:
            ingamebackground.image = ingamebackground.images[1]
        else:
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
    
def debug_lines():
    global ecran
    pygame.draw.line(ecran, (66, 236, 255), (960,0), (960,1080), 1)
    pygame.draw.line(ecran, (66, 236, 255), (480,0), (480,1080), 1)
    pygame.draw.line(ecran, (66, 236, 255), (1440,0), (1440,1080), 1)
    
    pygame.draw.line(ecran, (66, 236, 255), (0,360), (1920,360), 1)
    pygame.draw.line(ecran, (66, 236, 255), (0,540), (1920,540), 1)
    pygame.draw.line(ecran, (66, 236, 255), (0,720), (1920,720), 1)

def draw_ending_text():

    timeleft_center_image1 = FontDel1.render(str(time_left), True, (0, 255, 0))
    timeleft_center_image2 = FontDel2.render(str(time_left), True, (0, 200, 0))
    timeleft_center_image1_width, timeleft_center_image1_height = timeleft_center_image1.get_rect().size
    ecran.blit(timeleft_center_image1,(1920/2 - timeleft_center_image1_width/2,1080/2 - timeleft_center_image1_height+20))
    ecran.blit(timeleft_center_image2,(1920/2 - timeleft_center_image1_width/2,1080/2 - timeleft_center_image1_height+20))
        
    HighScore_image1 = FontDel1.render("HIGH SCORE", True, (66, 236, 255))
    HighScore_image2 = FontDel2.render("HIGH SCORE", True, (66, 0, 255))
    HighScore_center_image1_width, HighScore_center_image1_height = HighScore_image1.get_rect().size
    ecran.blit(HighScore_image1,(1920/2 - HighScore_center_image1_width  / 2,5))
    ecran.blit(HighScore_image2,(1920/2 - HighScore_center_image1_width  / 2,5))

    HighScore_image1_text = FontDel1.render(str(high_score), True, (239, 41, 41))
    HighScore_image2_text = FontDel2.render(str(high_score), True, (204, 0, 0))
    HighScore_center_image1_text_width, HighScore_center_image1_text_height = HighScore_image1_text.get_rect().size
    ecran.blit(HighScore_image1_text,(1920/2 - HighScore_center_image1_text_width  / 2,185))
    ecran.blit(HighScore_image2_text,(1920/2 - HighScore_center_image1_text_width  / 2,185))
    
    
    YourScore_image1_text = FontDel1.render("YOUR SCORE", True, (66, 236, 255))
    YourScore_image2_text = FontDel2.render("YOUR SCORE", True, (66, 0, 255))
    YourScore_center_image1_text_width, YourScore_center_image1_text_height = YourScore_image1_text.get_rect().size
    ecran.blit(YourScore_image1_text,(1920/2 - YourScore_center_image1_text_width  / 2,540))
    ecran.blit(YourScore_image2_text,(1920/2 - YourScore_center_image1_text_width  / 2,540))
    
    YourScore_image1 = FontDel1.render(str(score), True, (66, 236, 255))
    YourScore_image2 = FontDel2.render(str(score), True, (66, 0, 255))
    YourScore_center_image1_width, YourScore_center_image1_height = YourScore_image1.get_rect().size
    ecran.blit(YourScore_image1,(1920/2 - YourScore_center_image1_width  / 2,720))
    ecran.blit(YourScore_image2,(1920/2 - YourScore_center_image1_width  / 2,720))

    
def draw_ingame_text():
    global ecran
                    
    if time_left <= 15:
        #red
        Arcade_center_image1 =FontDel1.render(str(time_left), True, (239, 41, 41))
        Arcade_center_image2 =FontDel2.render(str(time_left), True, (204, 0, 0))
    elif time_left <= 30:
        #orange
        Arcade_center_image1 = FontDel1.render(str(time_left), True, (252, 175, 62))
        Arcade_center_image2 = FontDel2.render(str(time_left), True, (245, 121, 0))
    elif time_left <= 45:
        #yellow
        Arcade_center_image1 = FontDel1.render(str(time_left), True, (252, 233, 79))
        Arcade_center_image2 = FontDel2.render(str(time_left), True, (237, 212, 0))
    elif time_left >= 60:
        #green
        Arcade_center_image1 = FontDel1.render(str(time_left), True, (0, 255, 0))
        Arcade_center_image2 = FontDel2.render(str(time_left), True, (0, 200, 0))
    else:
        #green
        Arcade_center_image1 = FontDel1.render(str(time_left), True, (0, 255, 0))
        Arcade_center_image2 = FontDel2.render(str(time_left), True, (0, 200, 0))
       
    Arcade_center_image1_width, Arcade_center_image1_height = Arcade_center_image1.get_rect().size
    ecran.blit(Arcade_center_image1,(1920/2 - Arcade_center_image1_width/2,1080/2 - Arcade_center_image1_height/2))
    ecran.blit(Arcade_center_image2,(1920/2 - Arcade_center_image1_width/2,1080/2 - Arcade_center_image1_height/2))

    Score_image1 = FontDel1.render("PTS : " + str(score), True, (66, 236, 255))
    ecran.blit(Score_image1,(10,106))
    Score_image2 = FontDel2.render("PTS : " + str(score), True, (66, 0, 255))
    ecran.blit(Score_image2,(10,106))

def draw_intro_text():

    timeleft_center_image1 = FontDel1.render(str(time_left), True, (0, 255, 0))
    timeleft_center_image2 = FontDel2.render(str(time_left), True, (0, 200, 0))
       
    timeleft_center_image1_width, timeleft_center_image1_height = timeleft_center_image1.get_rect().size
    ecran.blit(timeleft_center_image1,(1920/2 - timeleft_center_image1_width/2,1080/2 - timeleft_center_image1_height/2))
    ecran.blit(timeleft_center_image2,(1920/2 - timeleft_center_image1_width/2,1080/2 - timeleft_center_image1_height/2))
    
    HighScore_image1 = FontDel1.render("HIGH SCORE", True, bluelight)
    HighScore_image2 = FontDel2.render("HIGH SCORE", True, blue)
    HighScore_center_image1_width, HighScore_center_image1_height = HighScore_image1.get_rect().size
    ecran.blit(HighScore_image1,(1920/2 - HighScore_center_image1_width  / 2,5))
    ecran.blit(HighScore_image2,(1920/2 - HighScore_center_image1_width  / 2,5))

    HighScore_image1_text = FontDel1.render(str(high_score), True, bluelight)
    HighScore_image2_text = FontDel2.render(str(high_score), True, blue)
    HighScore_center_image1_text_width, HighScore_center_image1_text_height = HighScore_image1_text.get_rect().size
    ecran.blit(HighScore_image1_text,(1920/2 - HighScore_center_image1_text_width  / 2,185))
    ecran.blit(HighScore_image2_text,(1920/2 - HighScore_center_image1_text_width  / 2,185))
    

#initialise background table
introbackground = BackgroudFrame()
ingamebackground = Background()
camring = ColoredRing()

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
            
  
            Decalagex = (LARGEUR_ECRAN - mycam.LargeurChampCamera) / 2 
            ingamebackground.image = ingamebackground.images[1]
        else:
            webcam_zone_interdite = False
            ingamebackground.image = ingamebackground.images[0]
    except:
        print("cam unsuported. CPU is too old")
        webcam_compatibility = False
        webcam_zone_interdite = False
        ingamebackground.image = ingamebackground.images[0]
        
else:
    webcam_compatibility = False
    webcam_zone_interdite = False
    ingamebackground.image = ingamebackground.images[0]

# run the background game music
if background_music == True:
    music = pygame.mixer.Sound('./assets/Sounds/Neon City.mp3')
    channel1 = pygame.mixer.Channel(0)
    channel1.play(music, loops = -1)
    
    

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

        draw_intro_text()
        if debug_line == True:
            debug_lines()
        
        
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
        
        
        draw_ingame_text()
        
        #if mycam.zoneinterdite == True:
        #    ecran.blit(adervtising_shooting_zone.image, adervtising_shooting_zone.rect)
        
        if debug_line == True:
            debug_lines()

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

        draw_ending_text()
        
        if debug_line == True:
            debug_lines()
        
        pygame.display.flip()
        
        if time_left <= 0:
            next_gamestate()
    clock.tick(30)


pygame.quit
