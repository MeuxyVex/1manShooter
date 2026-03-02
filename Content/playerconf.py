import pygame
from .projectile import Projectile



class joueur(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.NewTaille = (300, 300)
        try:
            idle = pygame.image.load("Assets/file.png")
        except Exception:
            idle = pygame.Surface(self.NewTaille)
            idle.fill((255, 0, 255))
        self.image_idle = pygame.transform.scale(idle, self.NewTaille)

        try:
            jump_img = pygame.image.load("Assets/jump.png")
        except Exception:
            jump_img = self.image_idle.copy()
        self.image_jump = pygame.transform.scale(jump_img, self.NewTaille)


        self.image = self.image_idle

        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 300

        self.PV = 100
        self.MAX_PV = 100
        self.attaque = 10
        self.vitesse = 3
        self.jumppower = -20
        self.gravity = 1
        self.velocity_y = 0
        self.on_ground = True
        self.all_projectiles = pygame.sprite.Group()
        self.clock = pygame.time.Clock()


    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))
    

    def move_right(self):
        self.rect.x += self.vitesse
    
    def move_left(self):
        self.rect.x -= self.vitesse
    
    def move_jump(self):
        if self.on_ground:
            self.velocity_y = self.jumppower
            self.on_ground = False
            self.image = self.image_jump
    

    def applygravity(self, platform_rect):
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        if self.rect.colliderect(platform_rect) and self.velocity_y >= 0:
            self.rect.bottom = platform_rect.top
            self.velocity_y = 0
            self.on_ground = True
            self.image = self.image_idle
        else:
            self.on_ground = False


