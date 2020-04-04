import pygame
from constants import BLOCK_IMG_PATH, WIDTH, BLOCK_WIDTH

class Block(pygame.sprite.Sprite):
    def __init__(self, playerYPosition):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(BLOCK_IMG_PATH).convert()
        self.rect = self.image.get_rect()
        self.rect.centery = playerYPosition
        self.rect.x = WIDTH - self.rect.width - 20
        self.speedx = -15

    def update(self):
        self.rect.x += self.speedx
        if (self.rect.x + BLOCK_WIDTH < 0):
            self.kill()