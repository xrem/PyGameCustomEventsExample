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
        self.state_verical = STATE_IDLE
        self.state_horizontal = STATE_IDLE
        self.speed = 5
        self.hp = 100

    def set_state_verical(self, state):
        self.state_verical = state

    def set_state_horizontal(self, state):
        self.state_horizontal = state

    def update(self):
        if (self.hp < 100 and self.hp > 0):
            self.hp += 0.10

        self.rect.y += self.speed * self.state_verical
        self.rect.x += self.speed * self.state_horizontal

        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y + self.rect.height >= HEIGHT:
            self.rect.y = HEIGHT - self.rect.height

        if self.rect.x <= 10:
            self.rect.x = 10
        if self.rect.x >= 300:
            self.rect.x = 300

        if pygame.sprite.groupcollide(self.player_group, self.blocks, False, True):
           self.hp -= 40
           if (self.hp <= 0):
               self.kill()
