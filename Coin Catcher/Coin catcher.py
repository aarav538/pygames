import pygame
from pygame.locals import *
import random

pygame.font.get_fonts()

pygame.init()

ww = 1200
wh = 900

w = pygame.display.set_mode((ww,wh))
pygame.display.set_caption("Coin Catcher")

p_image = pygame.image.load("Images/player.png")
p_rect = p_image.get_rect()
p_speed = 1
p_rect.y = 400
p_rect.x = 500

c_image = pygame.image.load("Images/coin.png")
c_rect = p_image.get_rect()
c_rect.y = random.randint(0,800)
c_rect.x = random.randint(0,800)

font = pygame.font.SysFont("lucidaconsole", 100)
score = 0

run = True

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        p_rect.y -= p_speed
    if keys[K_DOWN]:
        p_rect.y += p_speed
    if keys[K_LEFT]:
        p_rect.x -= p_speed
    if keys[K_RIGHT]:
        p_rect.x += p_speed

    if p_rect.y <= 0:
        p_rect.y = 1
    if p_rect.y >= 800:
        p_rect.y = 800
    if p_rect.x <= 0:
        p_rect.x = 1
    if p_rect.x >= 900:
        p_rect.x = 900

    w.fill((255, 255, 255))
    w.blit(p_image, p_rect)
    w.blit(c_image, c_rect)

    if p_rect.colliderect(c_rect):
        c_rect.y = random.randint(0,800)
        c_rect.x = random.randint(0,800)
        score += 1

    s_text = font.render(f"{score}", True, (0, 0, 0))
    g_text = font.render("Coin Catcher", True, (0, 0, 0))
    w.blit(s_text, (ww // 2 - s_text.get_width() // 2, 350))
    w.blit(g_text, (ww // 2 - g_text.get_width() // 2, 50))

    pygame.display.update()
pygame.quit()
