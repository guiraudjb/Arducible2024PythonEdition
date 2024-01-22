#---------------------------------IMPORTS-------------------------------
import pygame
from pygame import *
pygame.init()
from Scripts.init import * # load config.ini and some variables
from Scripts.Sprites import *# load sprites

#---------------------Procedures et fonctions---------------------------

def init_game():
    global cible1
    global cible2
    global cible3
    cible1 = Cible()
    #cible1.image = pygame.transform.scale(cible1.image, (LARGEUR_ECRAN*0.2, HAUTEUR_ECRAN*0.35))
    cible1.rect.x = LARGEUR_ECRAN*0.15 - LARGEUR_ECRAN*0.2/2
    cible1.rect.y = HAUTEUR_ECRAN * 0.82 - HAUTEUR_ECRAN*0.35/2

    cible2 = Cible()
    #cible2.image = pygame.transform.scale(cible2.image, (LARGEUR_ECRAN*0.2, HAUTEUR_ECRAN*0.35))
    cible2.rect.x = LARGEUR_ECRAN/2 - LARGEUR_ECRAN*0.2/2
    cible2.rect.y = HAUTEUR_ECRAN * 0.82 - HAUTEUR_ECRAN*0.35/2

    cible3 = Cible()
    cible3.image = cible3.images[1]
    #cible3.image = pygame.transform.scale(cible3.image, (LARGEUR_ECRAN*0.2, HAUTEUR_ECRAN*0.35))
    cible3.rect.x = LARGEUR_ECRAN*0.85 - LARGEUR_ECRAN*0.2/2
    cible3.rect.y = HAUTEUR_ECRAN * 0.82 - HAUTEUR_ECRAN*0.35/2
    
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
            ingamebackground.image = pygame.transform.scale(ingamebackground.image, (LARGEUR_ECRAN, HAUTEUR_ECRAN))

        else:
            ingamebackground.image = ingamebackground.images[0]
            ingamebackground.image = pygame.transform.scale(ingamebackground.image, (LARGEUR_ECRAN, HAUTEUR_ECRAN))

        time_left = game_length
        score = 0
    elif gamestate == 1:
        gamestate = 2
        ingamebackground.image = ingamebackground.images[2]
        ingamebackground.image = pygame.transform.scale(ingamebackground.image, (LARGEUR_ECRAN, HAUTEUR_ECRAN))

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
    ecran.blit(mycam.images, (LARGEUR_ECRAN/2-mycam.width/2,0))
 
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

def draw_camring():
    global ecran
    global camring

    if mycam.zoneinterdite == True:
        draw_go_to_shooting_zone()
        camring.image = camring.images[0]
        ecran.blit(camring.image, camring.rect)
    else:
        camring.image = camring.images[1]
        ecran.blit(camring.image, camring.rect)
    
    
def debug_lines():
    global ecran
    pygame.draw.line(ecran, red, (LARGEUR_ECRAN/2,0), (960,HAUTEUR_ECRAN), 1)
    pygame.draw.line(ecran, red, (480,0), (480,HAUTEUR_ECRAN), 1)
    pygame.draw.line(ecran, red, (1440,0), (1440,HAUTEUR_ECRAN), 1)
    
    pygame.draw.line(ecran, red, (0,360), (LARGEUR_ECRAN,360), 1)
    pygame.draw.line(ecran, red, (0,HAUTEUR_ECRAN/2), (LARGEUR_ECRAN,HAUTEUR_ECRAN/2), 1)
    pygame.draw.line(ecran, red, (0,HAUTEUR_ECRAN*2/3), (LARGEUR_ECRAN,HAUTEUR_ECRAN*2/3), 1)

def draw_go_to_shooting_zone():
    getaway_center_image1 = FontDel1.render("Go to the shooting zone", True, redlight)
    getaway_center_image2 = FontDel2.render("Go to the shooting zone", True, red)
       
    getaway_center_image1_width, getaway_center_image1_height = getaway_center_image1.get_rect().size
    ecran.blit(getaway_center_image1,(LARGEUR_ECRAN/2 - getaway_center_image1_width/2, HAUTEUR_ECRAN*55/100))
    ecran.blit(getaway_center_image2,(LARGEUR_ECRAN/2 - getaway_center_image1_width/2, HAUTEUR_ECRAN*55/100))


def draw_intro_text():

    timeleft_center_image1 = FontDel1.render(str(time_left), True, bluelight)
    timeleft_center_image2 = FontDel2.render(str(time_left), True, blue)
       
    timeleft_center_image1_width, timeleft_center_image1_height = timeleft_center_image1.get_rect().size
    ecran.blit(timeleft_center_image1,(LARGEUR_ECRAN/2 - timeleft_center_image1_width/2,HAUTEUR_ECRAN/2 - timeleft_center_image1_height/2))
    ecran.blit(timeleft_center_image2,(LARGEUR_ECRAN/2 - timeleft_center_image1_width/2,HAUTEUR_ECRAN/2 - timeleft_center_image1_height/2))
    
    HighScore_image1 = FontDel1.render("HIGH SCORE", True, bluelight)
    HighScore_image2 = FontDel2.render("HIGH SCORE", True, blue)
    HighScore_center_image1_width, HighScore_center_image1_height = HighScore_image1.get_rect().size
    ecran.blit(HighScore_image1,(LARGEUR_ECRAN/2 - HighScore_center_image1_width  / 2,5))
    ecran.blit(HighScore_image2,(LARGEUR_ECRAN/2 - HighScore_center_image1_width  / 2,5))

    HighScore_image1_text = FontDel1.render(str(high_score), True, bluelight)
    HighScore_image2_text = FontDel2.render(str(high_score), True, blue)
    HighScore_center_image1_text_width, HighScore_center_image1_text_height = HighScore_image1_text.get_rect().size
    ecran.blit(HighScore_image1_text,(LARGEUR_ECRAN/2 - HighScore_center_image1_text_width  / 2,HighScore_center_image1_text_height))
    ecran.blit(HighScore_image2_text,(LARGEUR_ECRAN/2 - HighScore_center_image1_text_width  / 2,HighScore_center_image1_text_height))
   
    
def draw_ingame_text():
    global ecran
                    
    if time_left <= 15:
        #red
        Arcade_center_image1 =FontDel1.render(str(time_left), True, redlight)
        Arcade_center_image2 =FontDel2.render(str(time_left), True, red)
    elif time_left <= 30:
        #orange
        Arcade_center_image1 = FontDel1.render(str(time_left), True, orangelight)
        Arcade_center_image2 = FontDel2.render(str(time_left), True, orange)
    elif time_left <= 45:
        #yellow
        Arcade_center_image1 = FontDel1.render(str(time_left), True, yellowlight)
        Arcade_center_image2 = FontDel2.render(str(time_left), True, yellow)
    elif time_left >= 60:
        #green
        Arcade_center_image1 = FontDel1.render(str(time_left), True, greenlight)
        Arcade_center_image2 = FontDel2.render(str(time_left), True, green)
    else:
        #green
        Arcade_center_image1 = FontDel1.render(str(time_left), True, greenlight)
        Arcade_center_image2 = FontDel2.render(str(time_left), True, green)
       
    Arcade_center_image1_width, Arcade_center_image1_height = Arcade_center_image1.get_rect().size
    ecran.blit(Arcade_center_image1,(LARGEUR_ECRAN/2 - Arcade_center_image1_width/2,HAUTEUR_ECRAN/2 - Arcade_center_image1_height/2))
    ecran.blit(Arcade_center_image2,(LARGEUR_ECRAN/2 - Arcade_center_image1_width/2,HAUTEUR_ECRAN/2 - Arcade_center_image1_height/2))
    
    
    Score_image1_text = FontDel1.render("POINTS", True, bluelight)
    Score_image2_text = FontDel2.render("POINTS", True, blue)
    Score_image1_text_width, Score_image1_text_height = Score_image1_text.get_rect().size
   
    ecran.blit(Score_image1_text,(LARGEUR_ECRAN/5 - Score_image1_text_width/2,Score_image1_text_height/2))
    ecran.blit(Score_image2_text,(LARGEUR_ECRAN/5 - Score_image1_text_width/2,Score_image1_text_height/2))
    
    Score_image1 = FontDel1.render(str(score), True, bluelight)
    Score_image2 = FontDel2.render(str(score), True, blue)
    Score_image1_width, Score_image1_height = Score_image1.get_rect().size
   
    ecran.blit(Score_image1,(LARGEUR_ECRAN/5 - Score_image1_width/2,HAUTEUR_ECRAN/3 - Score_image1_height/2))
    ecran.blit(Score_image2,(LARGEUR_ECRAN/5 - Score_image1_width/2,HAUTEUR_ECRAN/3 - Score_image1_height/2))



def draw_ending_text():

    timeleft_center_image1 = FontDel1.render(str(time_left), True, greenlight)
    timeleft_center_image2 = FontDel2.render(str(time_left), True, green)
    timeleft_center_image1_width, timeleft_center_image1_height = timeleft_center_image1.get_rect().size
    ecran.blit(timeleft_center_image1,(LARGEUR_ECRAN/2 - timeleft_center_image1_width/2,HAUTEUR_ECRAN/2 - timeleft_center_image1_height))
    ecran.blit(timeleft_center_image2,(LARGEUR_ECRAN/2 - timeleft_center_image1_width/2,HAUTEUR_ECRAN/2 - timeleft_center_image1_height))
        
    HighScore_image1 = FontDel1.render("HIGH SCORE", True, bluelight)
    HighScore_image2 = FontDel2.render("HIGH SCORE", True, blue)
    HighScore_center_image1_width, HighScore_center_image1_height = HighScore_image1.get_rect().size
    ecran.blit(HighScore_image1,(LARGEUR_ECRAN/2 - HighScore_center_image1_width  / 2,5))
    ecran.blit(HighScore_image2,(LARGEUR_ECRAN/2 - HighScore_center_image1_width  / 2,5))

    HighScore_image1_text = FontDel1.render(str(high_score), True, redlight)
    HighScore_image2_text = FontDel2.render(str(high_score), True, red)
    HighScore_center_image1_text_width, HighScore_center_image1_text_height = HighScore_image1_text.get_rect().size
    ecran.blit(HighScore_image1_text,(LARGEUR_ECRAN/2 - HighScore_center_image1_text_width  / 2,HighScore_center_image1_text_height))
    ecran.blit(HighScore_image2_text,(LARGEUR_ECRAN/2 - HighScore_center_image1_text_width  / 2,HighScore_center_image1_text_height))
    
    
    YourScore_image1_text = FontDel1.render("YOUR SCORE", True, yellowlight)
    YourScore_image2_text = FontDel2.render("YOUR SCORE", True, yellow)
    YourScore_center_image1_text_width, YourScore_center_image1_text_height = YourScore_image1_text.get_rect().size
    ecran.blit(YourScore_image1_text,(LARGEUR_ECRAN/2 - YourScore_center_image1_text_width  / 2,HAUTEUR_ECRAN/2))
    ecran.blit(YourScore_image2_text,(LARGEUR_ECRAN/2 - YourScore_center_image1_text_width  / 2,HAUTEUR_ECRAN/2))
    
    YourScore_image1 = FontDel1.render(str(score), True, yellowlight)
    YourScore_image2 = FontDel2.render(str(score), True, yellow)
    YourScore_center_image1_width, YourScore_center_image1_height = YourScore_image1.get_rect().size
    ecran.blit(YourScore_image1,(LARGEUR_ECRAN/2 - YourScore_center_image1_width  / 2,HAUTEUR_ECRAN*2/3))
    ecran.blit(YourScore_image2,(LARGEUR_ECRAN/2 - YourScore_center_image1_width  / 2,HAUTEUR_ECRAN*2/3))


def draw_cibles():
    global ecran
    global cible1
    global cible2
    global cible3
    global cibleencours
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
        
    
    #cible1.image = pygame.transform.scale(cible1.image, (LARGEUR_ECRAN*0.2, HAUTEUR_ECRAN*0.35))
    #cible2.image = pygame.transform.scale(cible2.image, (LARGEUR_ECRAN*0.2, HAUTEUR_ECRAN*0.35))
    #cible3.image = pygame.transform.scale(cible3.image, (LARGEUR_ECRAN*0.2, HAUTEUR_ECRAN*0.35))
    ecran.blit(cible1.image, cible1.rect)
    ecran.blit(cible2.image, cible2.rect)
    ecran.blit(cible3.image, cible3.rect)


#-------------------------DEBUT DU Programme ---------------------------
#initialise background table
introbackground = BackgroudFrame()
ingamebackground = Background()
ingamebackground.image = pygame.transform.scale(ingamebackground.image, (LARGEUR_ECRAN, HAUTEUR_ECRAN))
camring = ColoredRing()
camring_width, camring_height = camring.image.get_rect().size
camring.rect.x = LARGEUR_ECRAN/2 - camring_width/2

#initialise webcam if actived in config.ini
if active_webcam:
    try:
        from Scripts.opencvcam import Cam
        mycam = Cam()
        mycam.update(mycam.cap, mycam.mp_drawing,mycam.mp_pose, mycam.LimiteBasseCamera, mycam.LimiteHauteCamera, mycam.LimiteGaucheCamera, mycam.LimiteDroiteCamera)
        
        
        if mycam.webcam_compatibility == True:
            webcam_compatibility = True
        else:
            webcam_compatibility = False
            
        if webcam_compatibility == True:
            
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

#initialise the screen
pygame.display.set_caption("Arducible PÉTANQUE GAME") # set window title
if Fullscreen:
    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN), pygame.SCALED | pygame.FULLSCREEN, vsync=1)
else:
    ecran = pygame.display.set_mode((LARGEUR_ECRAN, HAUTEUR_ECRAN), pygame.SCALED )

# run the background game music
if background_music == True:
    music = pygame.mixer.Sound('./assets/Sounds/Neon City.mp3')
    channel1 = pygame.mixer.Channel(0)
    channel1.play(music, loops = -1)
    
    


init_game()


#---------------------------main game loop------------------------------

while continuer:
    #-----------------------begining scene------------------------------
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
        
        if ShowFPS == True:
            fps = str(int(clock.get_fps()))
            FPS1 = FontDel1.render(fps, True, blue)
            FPS2 = FontDel2.render(fps, True, bluelight)
            ecran.blit(FPS1,(0,0))
            ecran.blit(FPS2,(0,0))
        
        pygame.display.flip()
        if time_left <= 0:
            next_gamestate()
        
    #-----------------------Game scene----------------------------------
    if gamestate == 1:
        countdown()
        
        
        if webcam_compatibility == True:
            mycam.update(mycam.cap, mycam.mp_drawing,mycam.mp_pose, mycam.LimiteBasseCamera, mycam.LimiteHauteCamera, mycam.LimiteGaucheCamera, mycam.LimiteDroiteCamera)
            showcam()
            webcam_zone_interdite = mycam.zoneinterdite
            ecran.blit(ingamebackground.image, ingamebackground.rect)
            #ecran.blit(ingamebackground.image, ingamebackground.rect)
            if DebugCam == True:
               showcam()
            
            draw_camring()
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


        draw_cibles()
                
        draw_ingame_text()
        
        
        if debug_line == True:
            debug_lines()
        if ShowFPS == True:
            fps = str(int(clock.get_fps()))
            FPS1 = FontDel1.render(fps, True, blue)
            FPS2 = FontDel2.render(fps, True, bluelight)
            ecran.blit(FPS1,(0,0))
            ecran.blit(FPS2,(0,0))

        pygame.display.flip()
        
        if time_left <= 0:
            next_gamestate()

        #clock.tick(60)
    #-----------------------ending scene--------------------------------    
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
        
        if ShowFPS == True:
            fps = str(int(clock.get_fps()))
            FPS1 = FontDel1.render(fps, True, blue)
            FPS2 = FontDel2.render(fps, True, bluelight)
            ecran.blit(FPS1,(200,0))
            ecran.blit(FPS2,(200,0))
        
        pygame.display.flip()
        
        if time_left <= 0:
            next_gamestate()
            
    clock.tick(FPS) #set to 30 FPS
    
    

pygame.quit
