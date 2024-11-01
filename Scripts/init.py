import pygame
from pygame import *
import os.path
import configparser
import pygame
import random


#initialise timer for game
clock = pygame.time.Clock()
old_timer = pygame.time.get_ticks()
game_timer = pygame.time.get_ticks()

cam_clock = pygame.time.Clock()
old_cam_timer = pygame.time.get_ticks()
cam_timer = pygame.time.get_ticks()

channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
channel2.set_volume(0.1)

oldlevel = 0
level = 1
cibleencours = 2
score = 0
high_score = 0
gamestate = 0
oldcibleencours = cibleencours
continuer = True
current_time = 0
old_current_time = 0
affichage = True


# parse config.ini and create if not exist
if not os.path.exists("config.ini"):
    # Ouvrir le fichier en mode écriture
    f = open("config.ini", "w")
    # Écrire du texte dans le fichier
    f.write("[TimeSetting]\n")
    f.write("intro_length = 10\n")
    f.write("game_length = 60\n")
    f.write("ending_length = 10\n")
    f.write("\n")
    f.write("[BonusTime]\n")
    f.write("time = 5\n")
    f.write("\n")
    f.write("[CamActivation]\n")
    f.write("Webcam = True\n")
    f.write("\n")
    f.write("[Screen]\n")
    f.write("Fullscreen = True\n")
    f.write("\n")
    f.write("[Audio]\n")
    f.write("Music = True\n")
    f.write("Effects = True\n")
    f.write("FadeoutTime = 1000\n")
    f.write("\n")
    f.write("[Resolution]\n")
    f.write("#resolution value 1080 720 360 240 if empty resolution will be set to 1024x768\n")
    f.write("Resolution = 1080\n")
    f.write("\n")
    f.write("[Debug]\n")
    f.write("DebugLine = False\n")
    f.write("FPS = 20\n")
    f.write("ShowFps = False\n")
    f.write("DebugCam = False\n")
    f.write("Credit = 1\n")
    # Fermer le fichier
    f.close()



if os.path.exists("config.ini"):
    with open("config.ini", "r") as f:
        # Crée un objet ConfigParser
        config = configparser.ConfigParser()
        # Lit le fichier INI
        config.read_file(f)
        # Accédez aux données du fichier INI
        intro_length = int(config["TimeSetting"]["intro_length"])
        game_length = int(config["TimeSetting"]["game_length"])
        ending_length = int(config["TimeSetting"]["ending_length"])
        bonus_time = int(config["BonusTime"]["time"])
        active_webcam_string = (config["CamActivation"]["Webcam"])
        fullscreen_string = config["Screen"]["Fullscreen"]
        background_music_string = config["Audio"]["Music"]
        sound_effects_string = config["Audio"]["Effects"]
        FadeoutTime = int(config["Audio"]["FadeoutTime"])
        debug_line_string = (config["Debug"]["DebugLine"])
        resolution = int(config["Resolution"]["Resolution"])
        FPS = int(config["Debug"]["FPS"])
        ShowFps_string = config["Debug"]["ShowFps"]
        DebugCam_string = config["Debug"]["DebugCam"]
        credit_left = int(config["Debug"]["Credit"])
        f.close

time_left = intro_length

if resolution == 1080:
    LARGEUR_ECRAN = 1920
    HAUTEUR_ECRAN = 1080
elif resolution == 720:
    LARGEUR_ECRAN = 1280
    HAUTEUR_ECRAN = 720
elif resolution == 360:
    LARGEUR_ECRAN = 640
    HAUTEUR_ECRAN = 360
elif resolution == 240:
    LARGEUR_ECRAN = 426
    HAUTEUR_ECRAN = 240
else:
    LARGEUR_ECRAN = 1024
    HAUTEUR_ECRAN = 768

STR="résolution " + str(LARGEUR_ECRAN) + " X " + str(HAUTEUR_ECRAN)
print(STR)

Fontsize = round(HAUTEUR_ECRAN/10)
Fontsize2 = round(HAUTEUR_ECRAN/20)
#initialise font text
FontDel1 = pygame.font.Font("./assets/fonts/NEON GLOW.otf",Fontsize)
FontDel2 = pygame.font.Font("./assets/fonts/NEON GLOW-Hollow.otf",Fontsize)
FontDel3 = pygame.font.Font("./assets/fonts/NEON GLOW.otf",Fontsize2)
FontDel4 = pygame.font.Font("./assets/fonts/NEON GLOW-Hollow.otf",Fontsize2)
#preset color for neon font
red = (204, 0, 0)
redlight = (239, 41, 41)
orange = (245, 121, 0)
orangelight = (252, 175, 62)
yellow = (237, 212, 0)
yellowlight =(255, 255, 79)
blue = (66, 0, 255)
bluelight =(66, 236, 255)
green = (0, 255, 0)
greenlight = (0, 200, 0)


if active_webcam_string == 'True':
    active_webcam = True
else:
    active_webcam = False

if fullscreen_string == 'True':
    Fullscreen = True
else:
    Fullscreen = False
    

if background_music_string == 'True':
    background_music = True
else:
    background_music = False
    
if sound_effects_string == 'True':
    sound_effects = True
else:
    sound_effects = False
    
if debug_line_string == 'True':
    debug_line = True
else:
    debug_line = False
    
if ShowFps_string == 'True':
    ShowFPS = True
else:
    ShowFPS = False
    
if DebugCam_string == 'True':
    DebugCam = True
else:
    DebugCam = False

waiting = True


