import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((128, 128, 128))  # Grey color for obstacles
        self.rect = self.image.get_rect(topleft=(x, y))