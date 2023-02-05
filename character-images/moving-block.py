import pygame
pygame.init()

window_width = 500
window_hight = 480
game_window = pygame.display.set_mode((window_width,window_hight))
# Give the window a name
pygame.display.set_caption('First game')

image_walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
image_walk_left = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
background = pygame.image.load('bg.jpg')
image_stop_character = pygame.image.load('standing.png')
  
# Define the character
x, y = 50, 400 # Character position
character_width = 40
character_height = 60
vel = 5 # The velocity that the character moves in the screen

clock = pygame.time.Clock()

is_jump = False
jump_count = 10

walk_left = False
walk_right = False
walk_count = 0



def redraw_game_window():
    global walk_count

    game_window.blit(background, (0,0))
    if walk_count + 1 >= 27: # 27/3 = 9 number of images per walk side  ( +1 ?????????)
        walk_count = 0 

    if walk_left:
        game_window.blit(image_walk_left[walk_count//3], (x,y))
        walk_count += 1
    elif walk_right:
        game_window.blit(image_walk_right[walk_count//3], (x,y))
        walk_count += 1
    else:
        game_window.blit(image_stop_character, (x,y))
        walk_count = 0
    pygame.display.update()
    
prog_run = True
while prog_run:
    clock.tick(27) # Define the game in 27 frames per second 
    
    for event in pygame.event.get():
        # QUIT means the 'X' that we normally close windows in the right upper corner
        if event.type == pygame.QUIT: 
            prog_run = False

        
    # The variable keys recieves a dictionary and pygame.K_[TECLA] is the key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
        walk_left = True
        walk_right = False
    elif keys[pygame.K_RIGHT] and x < (window_width - character_width):
        x += vel
        walk_left = False
        walk_right = True
    elif keys[pygame.K_SPACE]:
        is_jump = True
        walk_count = 0
    else:
        walk_left = False
        walk_right = False
         
    if is_jump:
        if jump_count > 0:
            y -= (jump_count ** 2) * 0.5
            jump_count -= 1
        elif jump_count >= -10:
            y += (jump_count ** 2) * 0.5
            jump_count -= 1
        else:
            jump_count = 10
            is_jump = False
           
    # Lets draw the character
    redraw_game_window()
    
pygame.quit()
