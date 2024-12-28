import pygame
class joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.PV = 100
        self.MAX_PV = 100
        self.attaque = 10
        self.vitesse = 5
        self.image = pygame.image.load("Assets/file.png")
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 600