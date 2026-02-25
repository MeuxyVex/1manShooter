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

#fenetre
pygame.display.set_caption("Smash1v1")
screen = pygame.display.set_mode((1536, 1024))  
image = pygame.image.load("assets/background.jpg")

#jeu
jeu = True
game = maingame()

while jeu:

    #fenetre
    screen.blit(image, (0, 0))
    # apliquer image
    screen.blit(game.Player.image, game.Player.rect)

    #apliquer toute les images
    game.Player.all_projectiles.draw(screen)

    #projectile joueur
    for projectile in game.Player.all_projectiles:
        projectile.deplacement()

    #gauche ou droit
    if game.press.get(pygame.K_RIGHT) and game.Player.rect.x + game.Player.rect.width < screen.get_width():
        game.Player.move_right()
    elif game.press.get(pygame.K_LEFT) and game.Player.rect.x > 0:
        game.Player.move_left()
    

    #ecran mis a jour 
    pygame.display.flip()
    
    #quit
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False
            pygame.quit()
            print("Fermeture du jeu")

        #deplacement
        elif event.type == pygame.KEYDOWN:
            game.press[event.key] = True

            if event.key == pygame.K_SPACE:
                game.Player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.press[event.key] = False
        
