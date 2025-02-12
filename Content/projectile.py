import pygame

#class projectile
class Projectile(pygame.sprite.Sprite):
    #constructeur
    def __init__(self, player):
        super().__init__()
        self.vitesse = 5
        self.player = player
        self.image = pygame.image.load("assets/projectile.jpg")
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 240
        self.rect.y = player.rect.y + 230
        self.origin_image = self.image
        self.angle = 0
    def rotation(self):
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center = self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def deplacement(self):
        self.rect.x += self.vitesse
        self.rotation()

        if self.rect.x > 2060:
            self.remove()
