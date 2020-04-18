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

#polygon(surface, color, points, width=0)

p1 = (300, 300)
p2 = (200, 500)
p3 = (400, 500)


player = Player(blocks)
all_sprite.add(player)

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, x, y):
    font = pygame.font.Font(font_name, 18)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_player_health(screen, player):
    outline = pygame.Rect(WIDTH - 110, 60, 100, 20)
    fill = pygame.Rect(WIDTH - 110, 60, player.hp, 20)
    fill_color = GREEN
    if player.hp <= 70:
        fill_color = YELLOW
    if player.hp <= 40:
        fill_color = RED

    if player.hp > 0:
        pygame.draw.rect(screen, GREY, outline)
        pygame.draw.rect(screen, fill_color, fill)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.set_state_verical(STATE_UP)
            if event.key == pygame.K_DOWN:
                player.set_state_verical(STATE_DOWN)
            if event.key == pygame.K_LEFT:
                player.set_state_horizontal(STATE_LEFT)
            if event.key == pygame.K_RIGHT:
                player.set_state_horizontal(STATE_RIGHT)
            if event.key == pygame.K_KP_PLUS:
                blocks_add_timer -= 100
                if (blocks_add_timer <= 100):
                    blocks_add_timer = 100
                pygame.time.set_timer(ADDBLOCK, blocks_add_timer)
            if event.key == pygame.K_KP_MINUS:
                if (blocks_add_timer >= 3000):
                    blocks_add_timer = 3000
                blocks_add_timer += 100
                pygame.time.set_timer(ADDBLOCK, blocks_add_timer)
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_UP and player.state_verical == STATE_UP) or\
                    (event.key == pygame.K_DOWN and player.state_verical == STATE_DOWN):
                player.set_state_verical(STATE_IDLE)
            if (event.key == pygame.K_LEFT and player.state_horizontal == STATE_LEFT) \
                    or (event.key == pygame.K_RIGHT and player.state_horizontal == STATE_RIGHT):
                player.set_state_horizontal(STATE_IDLE)
        if event.type == ADDBLOCK:
            block = Block(player.rect.centery)
            all_sprite.add(block)
            blocks.add(block)

    if player.hp <= 0:
        pygame.time.set_timer(ADDBLOCK, 0)

    all_sprite.update()
    screen.fill(BLACK)
    draw_text(screen, "Speed: "+str((3000 - blocks_add_timer) / 100), WIDTH - 50, 30)
    all_sprite.draw(screen)
    draw_player_health(screen, player)
    pygame.display.flip()

    clock.tick(FPS)