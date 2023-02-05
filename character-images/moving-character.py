import pygame
pygame.init

clock = pygame.time.Clock()

window_width = 500
window_hight = 480
game_window = pygame.display.set_mode((window_width,window_hight))

image_walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), 
pygame.image.load('R3.png'), pygame.image.load('R4.png'), 
pygame.image.load('R5.png'), pygame.image.load('R6.png'),
pygame.image.load('R7.png'), pygame.image.load('R8.png'),
pygame.image.load('R9.png')]

image_walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'),
pygame.image.load('L3.png'), pygame.image.load('L4.png'),
pygame.image.load('L5.png'), pygame.image.load('L6.png'),
pygame.image.load('L7.png'), pygame.image.load('L8.png'),
pygame.image.load('L9.png')]

background = pygame.image.load('bg.jpg')
image_stop_character = pygame.image.load('standing.png')

class Player:
    
    def __init__(self):
        self.x,self.y = 50,400
        self.width = 40
        self.height = 60
        self.velocity = 5

        self.jump_count = 0
        self.is_jump = False 
        
        self.walk_left = False
        self.walk_right = False
        self.walk_count = 0

    def draw(self,window):

        if self.walk_count + 1 >= 27:
            self.walk_count = 0
        
        if self.walk_left:
            window.blit(image_walk_left[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        elif self.walk_right:
            window.blit(image_walk_right[self.walk_count//3], (self.x, self.y))
            self.walk_count += 1
        else:
            self.walk_count = 0
            window.blit(image_stop_character, (self.x, self.y))

def redraw_game_window(player,window):
    # Add the background
    window.blit(background, (0,0))
    # Add the player
    player.draw(window)
    
    pygame.display.update()

# Game main loop

player = Player()
prog_run = True
while prog_run:
    clock.tick(27) # Make the fresh rate lower than 27 fps 

    for event in pygame.event.get():
    # QUIT means the 'X' that we normally close windows in the right upper corner
        if event.type == pygame.QUIT: 
            prog_run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.walk_left = True
        player.walk_right = False
        if player.x > 0 :
            player.x -= player.velocity

    elif keys[pygame.K_RIGHT]:
        player.walk_left = False
        player.walk_right = True
        if player.x < window_width - 64 :
            player.x += player.velocity
    elif keys[pygame.K_SPACE] and not player.is_jump:
        player.is_jump = True
        player.jump_count = 10
    else:
        player.walk_left = False
        player.walk_right = False
        

    if player.is_jump:        
  
        if player.jump_count > 0:
            player.y = (player.y - (player.jump_count**2)* 0.5)
            player.jump_count -= 1
        elif player.jump_count <= 0 and player.jump_count >= - 10:
            player.y = (player.y + (player.jump_count**2)* 0.5)
            player.jump_count -= 1
        else:
            player.jump_count = 0 
            player.is_jump = False          
    redraw_game_window(player, game_window)
                


                



