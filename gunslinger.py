import pygame
pygame.init

clock = pygame.time.Clock()

window_width = 500
window_hight = 480
game_window = pygame.display.set_mode((window_width,window_hight))


background = pygame.image.load('bg.jpg')


class element:
    def __init__(self,x,y,width,height,velocity):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.velocity = velocity
        self.hitbox = ()

class Player(element):
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

    def __init__(self):
        element.__init__(self,50,400,64,64,5)

        self.hitbox = (self.x + 17, self.y + 11, 25, 52 )
        self.jump_count = 0
        self.is_jump = False 
        
        self.stand = True
        self.walk_left = False
        self.walk_right = False
        self.walk_count = 0

    def draw(self,window):

        if not self.stand:
            if self.walk_count + 1 >= 27:
                self.walk_count = 0
            
            if self.walk_left:
                window.blit(self.image_walk_left[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
            else:
                window.blit(self.image_walk_right[self.walk_count//3], (self.x, self.y))
                self.walk_count += 1
        else:
            if self.walk_left:
                window.blit(self.image_walk_left[self.walk_count//3], (self.x, self.y))
            else:
                window.blit(self.image_walk_right[self.walk_count//3], (self.x, self.y))
        # pygame.draw.rect(window,(255,0,0), self.hitbox,2)

    def hit(self):
        print('PLAYER HIT')
class Enemy(element):
    image_walk_right = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    image_walk_left = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self,x,y):
        element.__init__(self,x,y,64,64,3)

        self.hitbox = (self.x + 17, self.y +2, 31, 57 )
        self.walk_count = 0
        self.walk_right = False
        self.walk_left = True

    def draw(self,window):
        self.move()
        # Each image will be used in 3 frames
        if self.walk_count +1 >= 33:
            self.walk_count = 0
        
        # test if i need the self in image
        if self.walk_left:
            window.blit(self.image_walk_left[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1
        elif self.walk_right:
            window.blit(self.image_walk_right[self.walk_count//3], (self.x,self.y))
            self.walk_count += 1 
        # pygame.draw.rect(window,(255,0,0), self.hitbox,2)
    def hit(self):
        print('ENEMY HIT')

    def move(self):
        if self.x <= 0:
            self.walk_left = False
            self.walk_right = True
            self.walk_count = 0
        elif self.x >= window_width - self.width:
            self.walk_left = True
            self.walk_right = False
            self.walk_count = 0

        if self.walk_left:
            self.x -= self.velocity
        elif self.walk_right:
            self.x += self.velocity
        self.hitbox = (self.x + 17, self.y +2, 31, 57 )

            
class projectile(element):

    def __init__(self,x,y,facing):
        element.__init__(self,x,y,10,3,15)
        # 1 = right, -1 = left
        self.facing = facing

    def draw(self,window):  
        pygame.draw.rect(window, (0,0,0), (self.x,self.y,self.width,self.height))

def redraw_game_window(player,bullets,enemies,window): 
    # Add the background
    window.blit(background, (0,0))
    # Add the player
    player.draw(window)

    [bullet.draw(window) for bullet in bullets]
    [enemy.draw(window) for enemy in enemies]
    pygame.display.update()

# Game main loop

player = Player()
bullets=[]
prog_run = True
enemies = []
enemies.append(Enemy(300,400)) # Enemy initial position
enemies.append(Enemy(100,400))


while prog_run:
    clock.tick(27) # Make the fresh rate lower than 27 fps 
    for event in pygame.event.get():
    # QUIT means the 'X' that we normally close windows in the right upper corner
        if event.type == pygame.QUIT: 
            prog_run = False
    
    # Bullet collision
    for bullet in bullets:
        for i in range(len(enemies)):
            if bullet.y > enemies[i].y and bullet.y < enemies[i].y + enemies[i].height and bullet.x > enemies[i].x and bullet.x < enemies[i].x + enemies[i].width:
                enemies[i].hit()
                if bullet in bullets: # If used to prevent error in the bullet removal    
                    bullets.pop(bullets.index(bullet))
        if bullet.x < 0 or bullet.x > 500:
            bullets.pop(bullets.index(bullet))
        else:
            bullet.x = bullet.x + bullet.facing * bullet.velocity

    # Characters collision
    for enemy in enemies:
        if (player.hitbox[1] + player.hitbox[2]) > enemy.hitbox[1]:
            
            if enemy.hitbox[0]< player.hitbox[0] < (enemy.hitbox[0] + enemy.hitbox[2]):
                player.hit()
            elif enemy.hitbox[0] < (player.hitbox[0] + player.hitbox[2]) < (enemy.hitbox[0] + enemy.hitbox[2]):
                player.hit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if player.walk_left:
            facing = -1
        else:
            facing = 1 

        if len(bullets) < 6:  
            bullets.append(projectile((player.x + player.width//2),(player.y + player.height//1.5),facing))
        

    if keys[pygame.K_LEFT]:
        player.stand = False
        player.walk_left = True
        player.walk_right = False
        if player.x > 0 :
            player.x -= player.velocity
    elif keys[pygame.K_RIGHT]:
        player.stand = False
        player.walk_left = False
        player.walk_right = True
        if player.x < window_width - 64 :
            player.x += player.velocity
    elif keys[pygame.K_UP] and not player.is_jump:
        player.stand = False
        player.is_jump = True
        player.jump_count = 10
    else:
        player.stand = True
        

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
    
    
    player.hitbox = (player.x + 17, player.y + 11, 25, 52 )
    redraw_game_window(player,bullets,enemies,game_window)
                


                



