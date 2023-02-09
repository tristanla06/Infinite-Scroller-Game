
import pygame, sys
from pygame import *

pygame.init()

# Window Settings
screen_width, screen_height = 1000, 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Player Movement and Collisions')

# Color Values
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Init font
font = pygame.font.Font(None, 30)

# Framerate
FPS = 60
frame_cap = pygame.time.Clock()

# Game Variables
speed = [2, -7]
x_acc = .1
y_acc = .1
default_pos = 700
jump = False
player_dead = False

class Background:
    def __init__(self, image):
        self.pic = pygame.image.load(image).convert()
        self.pic = pygame.transform.scale(self.pic, (screen_width, screen_height))
        self.width = self.pic.get_width()
        self.tiles = round(screen_width / self.width) + 1
        self.scroll = 0
    def image_scroll(self, scroll_speed, ground_y):
        for i in range(0, self.tiles):
            # draw a new image one after the other
            screen.blit(self.pic, (i * self.width + self.scroll, ground_y))
        # scroll left
        self.scroll -= scroll_speed
        # restart scroll
        if abs(self.scroll) > self.width:
            self.scroll = 0

# Parent Entity Class
class Entity:
    def __init__(self, width, height, x_pos, y_pos):      
            self.width = width
            self.height = height
            self.jump_vel = speed[1]
            self.rect = pygame.Rect(x_pos, y_pos, self.width, self.height)
    def get_properties(self):
        width_txt = font.render("player width: " + str(self.width), True, white)
        height_txt = font.render("player height: " + str(self.height), True, white)
        jump_txt = font.render("player bottom y: " + str(self.rect.bottom), True, white)
        collide_txt = font.render("player collide: " + str(player_dead ), True, white)
        screen.blit(width_txt, (10, 10))
        screen.blit(height_txt, (10, 30))
        screen.blit(jump_txt, (10, 50))
        screen.blit(collide_txt, (10, 70))

# Child Entity Class User
class Obstacle(Entity):
    def obs_move(self):
        self.rect.x -= speed[0]
        if self.rect.right < -40:
            self.rect.x = screen_width + 40             

# Child Entity Class User
class User(Entity):
    def player_jump(self):
        self.rect.y += speed[1]
        # Jump Movement and Velocity 
        if self.rect.bottom > 700:
            speed[1] = -1*speed[1]
        if speed[1] > 7:
            speed[1] = 7
        # Acceleration
        speed[1] += y_acc
    def player_shift(self):
        self.rect.x += speed[0]

# Call Background and Foreground Objects
bg = Background('Assets/background_glacial_mountains.png')

# Call Game Objects
player_1 = User(80, 200, 50, 500)
enemy_1 = Obstacle(80, 80, (screen_width + 40), 620)

# Game Functions
def update_screen():

    # Background
    screen.fill(black)
    player_1.get_properties()
    bg.image_scroll(2, 0)
    
    # Draw objects
    pygame.draw.rect(screen, red, player_1.rect)
    pygame.draw.rect(screen, green, enemy_1.rect)
    pygame.display.update()

def game_defaults():
    pass

# Game Loop
while True:
    frame_cap.tick(FPS)
    
    enemy_1.obs_move()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_SPACE:    
                jump = True

    # Checks the collision of the player and an enemy causing player death
    if (pygame.Rect.colliderect(player_1.rect, enemy_1.rect)):
        player_dead = True

    if not player_dead:
        # Player Jump Loop
        if jump:
            player_1.player_jump()
            # Stops the jump and sets y default        
            if player_1.rect.bottom > 700:
                jump = False
                speed[1] = -7
                player_1.rect.bottom = 700
    else:
        screen.blit
    update_screen()