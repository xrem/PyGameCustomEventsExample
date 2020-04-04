import pygame
from constants import PLAYER_IMG_PATH, HEIGHT, STATE_DOWN, STATE_IDLE, STATE_UP

class Player(pygame.sprite.Sprite):
    def __init__(self, blocks):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(PLAYER_IMG_PATH).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.centery = HEIGHT / 2
        self.blocks = blocks
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self)
        self.state = STATE_IDLE
        self.speed = 5

    def set_state(self, state):
        self.state = state

    def update(self):
        self.rect.y += self.speed * self.state
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y + self.rect.height >= HEIGHT:
            self.rect.y = HEIGHT - self.rect.height
        if pygame.sprite.groupcollide(self.player_group, self.blocks, False, False):
           self.kill()
