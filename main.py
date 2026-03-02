#!/usr/bin/python3
########################################################################################################
##########################################################################################################
#Verifcation de pip                                 
import subprocess
import sys
import importlib

import pygame.display                                                                       
def verifierpip():
    try:
        import pip
    except ImportError:
        print("Pip n'est pas encore installer, \nLancement de l'installation...")
        try:
            subprocess.check_call([sys.executable, "-m", "ensurepip", "--upgrade"])
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            print("Installer avec succès !")
            input("Appuyez sur Entrée pour continuer...")
            subprocess.Popen([sys.executable] + sys.argv)
            sys.exit()
        except subprocess.CalledProcessError:
            print("Echec de l'installation, nouvelle tentative...")
        import urllib.request
        import os
        url = "https://bootstrap.pypa.io/get-pip.py"
        get_pip = "get-pip.py"
        urllib.request.urlretrieve(url, get_pip)
        subprocess.check_call([sys.executable, get_pip])
        os.remove(get_pip)
        print("Installation réussi")
        input("Appuyez sur Entrée pour continuer...")
        subprocess.Popen([sys.executable] + sys.argv)
        sys.exit()
    else:
        print("PIP ✔️")
if __name__ == "__main__":
    verifierpip()

##########################################################################################################
##########################################################################################################
#Verification des packages 
def verifiepackage():
    installed = []
    packages = ["pygame"]
    for package in packages:
        try:
            importlib.import_module(package)
            installed.append(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", package])
            print(package, "Installés avec succès")
            installed.append(package)
    if len(installed) == len(packages):
        print("pygame✔️ ")
if __name__ == "__main__":
    verifiepackage()

###################MAIN###################################################################################




#main
import pygame
from Content import maingame, joueur
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Assets/theme.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1) 
#fenetre
pygame.display.set_caption("Smash1v1")
info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


#hitbox
platform_width = 1280
platform_heiht = 300
platform_x = (screen_width - platform_width) - 600 //2 
platform_y = screen_height // 2 + 80
platform_rect = pygame.Rect(platform_x, platform_y, platform_width, platform_heiht)


#image fond
image = pygame.image.load("assets/background.jpg")
image = pygame.transform.scale(image, (screen_width, screen_height))
#jeu
jeu = True
game = maingame()


#Debug 
print(f"debug {platform_rect.top}, {game.Player.rect}")


while jeu:


    #fenetre
    screen.blit(image, (0, 0))

    game.Player.applygravity(platform_rect)
    
    #Debug hitbox
    pygame.draw.rect(screen, (255, 0, 0), platform_rect, 2) 
    

    # apliquer image
    screen.blit(game.Player.image, game.Player.rect)

    #apliquer toute les images
    game.Player.all_projectiles.draw(screen)

    #projectile joueur
    for projectile in game.Player.all_projectiles:
        projectile.deplacement()

    #gauche ou droit
    if game.press.get(pygame.K_RIGHT):
        game.Player.move_right()
    elif game.press.get(pygame.K_LEFT):
        game.Player.move_left()

    
    #quit
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False
            pygame.quit()
            print("Fermeture du jeu")

        #deplacement
        elif event.type == pygame.KEYDOWN:
            game.press[event.key] = True

            if event.key == pygame.K_e:
                game.Player.launch_projectile()

            if event.key == pygame.K_SPACE:
                game.Player.move_jump()

        elif event.type == pygame.KEYUP:
            game.press[event.key] = False

    pygame.display.update()


            
            
        
