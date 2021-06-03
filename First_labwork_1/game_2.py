import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 700, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space  War")
# load images

RED_SPACE_SHIP = pygame.image.load(os.path.join("space_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("space_ship_green_small.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("space_ship_yellow.png"))
# main space shp

Blue_SPACE_SHIP = pygame.image.load(os.path.join("space_ship_blue.png"))

# laser
RED_LASER = pygame.image.load(os.path.join("laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("laser_green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("laser_yellow.png"))
BLUE_LASER = pygame.image.load(os.path.join("laser_blue.png"))

# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("SPACE_BG_6.0.png")), (WIDTH, HEIGHT))

class Ship:
    def __init__(self, x, y, color, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.Ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        '''pygame.drew.rect(WIN, (255, 0, 0), (self.x, self.y, 50, 50))'''
    def get_width(self):
        return  self.ship_img.get_width()
    def get_height(self):
        return self.ship_img.get_height()
class player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img =  YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

class Enemy(Ship):
    COLOR_MAP ={
               "red": (RED_SPACE_SHIP, RED_LASER),
               "green": (GREEN_SPACE_SHIP, GREEN_LASER),
               "yellow": (YELLOW_SPACE_SHIP, YELLOW_LASER)


    }
    def __init__(self, x, y, color, health=100): "red", "green", "blue"
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)
    def move(self, vel):
        self.y += vel

def main():
    run = True
    FPS = 60
    level = 1
    lives = 3
    main_font = pygame.font.SysFont("comicsans", 50)
    player_vel = 5

    Player = player(300, 650)
    clock = pygame.time.Clock()

    def redraw_window():
        WIN.blit(BG, (0, 0))

        # draw text
        lives_label = main_font.render(f"lives: {lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {level}", 1, (255, 255, 255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        player.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.k_a]:  # left
            player.x -= player_vel
            if keys[pygame.k_d]:  # right
                player.x += player_vel
            if keys[pygame.k_w]:  # up
                player.y -= player_vel
            if keys[pygame.k_s]:   #down
                player.y += player_vel

main()



