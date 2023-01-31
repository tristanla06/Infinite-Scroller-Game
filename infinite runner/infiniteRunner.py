import pygame, sys, math

pygame.init()

# window properties
screen_w, screen_h = 1000, 800
screen = pygame.display.set_mode((screen_w, screen_h))

# framerate values
FPS = 60
frame_cap = pygame.time.Clock()

class Ground:
    def __init__(self, image):
        self.pic = pygame.image.load(image).convert_alpha()
        self.width = self.pic.get_width()
        self.tiles = math.ceil(screen_w / self.width) + 1
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

# player class
class Player:
    def __init__(self):
        pass

# call background and foreground objects
bg = Ground('Assets/bg.png')
fg = Ground('Assets/fg.png')

def update_screen():
    pygame.display.update()


# game loop
while True:
    frame_cap.tick(FPS)
    
    # draw images
    bg.image_scroll(2, 0)
    fg.image_scroll(1, (screen_h / 1.9))

    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.quit()
                sys.exit()
    pygame.display.update()