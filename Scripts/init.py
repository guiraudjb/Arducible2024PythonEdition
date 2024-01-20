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

#initialise font text
GAME_FONT = pygame.font.Font("./assets/fonts/FUTRFW.TTF", 48)
Arcade_Font = pygame.font.Font("./assets/fonts/NeonSans.ttf", 196)
FONT = pygame.font.Font("./assets/fonts/NEON GLOW-Hollow.otf", 196)
FontDel2 = pygame.font.Font("./assets/fonts/NEON GLOW-Hollow.otf",196)
FontDel1 = pygame.font.Font("./assets/fonts/NEON GLOW.otf",196)

#FontDel1.set_bold(True)


LARGEUR_ECRAN =1920
HAUTEUR_ECRAN =1080
oldlevel = 0
level = 1
cibleencours = 2
score = 0
high_score = 0
gamestate = 0

oldcibleencours = cibleencours
continuer = True
debug_line = True

# parse config.ini and create if not exist
if not os.path.exists("config.ini"):
    # Ouvrir le fichier en mode écriture
    f = open("config.ini", "w")
    # Écrire du texte dans le fichier
    f.write("[TimeSetting]\n")
    f.write("intro_length = 5\n")
    f.write("game_length = 60\n")
    f.write("ending_length = 10\n")
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
    f.write("FadeoutTime = 3000\n")
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
        active_webcam_string = (config["CamActivation"]["Webcam"])
        fullscreen_string = config["Screen"]["Fullscreen"]
        background_music_string = config["Audio"]["Music"]
        sound_effects_string = config["Audio"]["Effects"]
        FadeoutTime = int(config["Audio"]["FadeoutTime"])
        f.close


time_left = intro_length

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
