import pygame
from .projectile import Projectile
class joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.PV = 100
        self.MAX_PV = 100
        self.attaque = 10
        self.vitesse = 3
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("Assets/file.png")
        self.NewTaille = (300,300)
        self.image = pygame.transform.scale(self.image, self.NewTaille)
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 230

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
    

    def move_right(self):
        self.rect.x += self.vitesse
    
    def move_left(self):
        self.rect.x -= self.vitesse