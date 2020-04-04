import pygame
from constants import *
from block import Block
from player import Player

running = True

pygame.init()
display_settings = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(display_settings)
all_sprite = pygame.sprite.Group()
blocks = pygame.sprite.Group()
clock = pygame.time.Clock()
blocks_add_timer = 1000
pygame.time.set_timer(ADDBLOCK, blocks_add_timer)

player = Player(blocks)
all_sprite.add(player)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, x, y):
    font = pygame.font.Font(font_name, 18)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.set_state(STATE_UP)
            if event.key == pygame.K_DOWN:
                player.set_state(STATE_DOWN)
            if event.key == pygame.K_LEFT:
                blocks_add_timer -= 100
                if (blocks_add_timer <= 100):
                    blocks_add_timer = 100
                pygame.time.set_timer(ADDBLOCK, blocks_add_timer)
            if event.key == pygame.K_RIGHT:
                if (blocks_add_timer >= 3000):
                    blocks_add_timer = 3000
                blocks_add_timer += 100
                pygame.time.set_timer(ADDBLOCK, blocks_add_timer)
        if event.type == pygame.KEYUP:
            player.set_state(STATE_IDLE)
        if event.type == ADDBLOCK:
            block = Block(player.rect.centery)
            all_sprite.add(block)
            blocks.add(block)

    all_sprite.update()
    screen.fill(BLACK)
    draw_text(screen, "Speed: "+str((3000 - blocks_add_timer) / 100), WIDTH - 50, 30)
    all_sprite.draw(screen)
    pygame.display.flip()

    clock.tick(FPS)