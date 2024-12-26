#!/usr/bin/python3
########################################################################################################
##########################################################################################################
#Verifcation de pip                                 
import subprocess
import sys
import importlib                                                                       
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
import pygame
pygame.init()

pygame.display.set_caption("OneManShooter")
pygame.display.set_mode((1920, 1080))
jeu = True
while jeu:
    for event  in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu = False
            pygame.quit()
            print("Fermeture du jeu")
