import pygame
import time
pygame.init


class element:
    def __init__(self,x,y,width,height,velocity):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.velocity = velocity
        self.hitbox = ()
        

class Player(element):

    image_walk_right = [pygame.image.load('Run (1)R.png'),pygame.image.load('Run (2)R.png'),pygame.image.load('Run (3)R.png'),pygame.image.load('Run (4)R.png'),pygame.image.load('Run (5)R.png'),pygame.image.load('Run (6)R.png'),pygame.image.load('Run (7)R.png')]
    image_stand_right = pygame.image.load('Idle (1)R.png')
    image_shoot_right = [pygame.image.load('Shoot (1)R.png'),pygame.image.load('Shoot (2)R.png'),pygame.image.load('Shoot (3)R.png')]
    image_jump_right = [pygame.image.load('Jump (1)R.png'),pygame.image.load('Jump (2)R.png'),pygame.image.load('Jump (3)R.png'),pygame.image.load('Jump (4)R.png'),pygame.image.load('Jump (5)R.png'),pygame.image.load('Jump (6)R.png'),pygame.image.load('Jump (7)R.png'),pygame.image.load('Jump (8)R.png'),pygame.image.load('Jump (9)R.png'),pygame.image.load('Jump (10)R.png')]
    image_dead_right = [pygame.image.load('Dead (1)R.png'),pygame.image.load('Dead (2)R.png'),pygame.image.load('Dead (3)R.png'),pygame.image.load('Dead (4)R.png'),pygame.image.load('Dead (5)R.png'),pygame.image.load('Dead (6)R.png'),pygame.image.load('Dead (7)R.png'),pygame.image.load('Dead (8)R.png'),pygame.image.load('Dead (9)R.png'),]

    image_walk_left = [pygame.image.load('Run (1)L.png'),pygame.image.load('Run (2)L.png'),pygame.image.load('Run (3)L.png'),pygame.image.load('Run (4)L.png'),pygame.image.load('Run (5)L.png'),pygame.image.load('Run (6)L.png'),pygame.image.load('Run (7)L.png')]
    image_stand_left = pygame.image.load('Idle (1)L.png')
    image_shoot_left = [pygame.image.load('Shoot (1)L.png'),pygame.image.load('Shoot (2)L.png'),pygame.image.load('Shoot (3)L.png')]
    image_jump_left = [pygame.image.load('Jump (1)L.png'),pygame.image.load('Jump (2)L.png'),pygame.image.load('Jump (3)L.png'),pygame.image.load('Jump (4)L.png'),pygame.image.load('Jump (5)L.png'),pygame.image.load('Jump (6)L.png'),pygame.image.load('Jump (7)L.png'),pygame.image.load('Jump (8)L.png'),pygame.image.load('Jump (9)L.png'),pygame.image.load('Jump (10)L.png')]




    def __init__(self):
        element.__init__(self,50,525,64,64,5)

        self.hitbox = (self.x + 38, self.y + 15, 66, 90)
        self.jump_count = 0
        self.is_jump = False 

        self.life = 100
        self.life_color = (0,255,0)
        self.life_count = 0
        
        self.stand = True
        self.walk_left = False
        self.walk_right = False
        self.walk_count = 0
        self.shooting = False
        

    def draw(self,window):

        if self.life <= 0:
            if self.life_count + 1 <= 24:
                window.blit(self.image_dead_right[self.life_count//3],(self.x,self.y))
                self.life_count += 1               
            else:
                quit()

            
            
        
        else:
            # Life bar color scale
            if self.life < (100/5)*1:
                self.life_color = (255,13,13)
            elif self.life < (100/5)*2:
                self.life_color = (255,78,17)
            elif self.life < (100/5)*3:
                self.life_color = (250,183,51)
            elif self.life < (100/5)*4:
                self.life_color = (172,179,52)
            else:
                self.life_color = (105,179,76)
            
            pygame.draw.rect(window,(0,0,0),(self.x + self.width/2.7,self.y - 10,100,10),2)
            pygame.draw.rect(window,self.life_color,(self.x + self.width/2.7,self.y - 10,self.life,10))

            if self.walk_count + 1 >= 21:
                    self.walk_count = 0

            if not self.stand:        
                if self.is_jump and self.walk_right:
                    window.blit(self.image_jump_right[int((self.jump_count+10)//2.1)],(self.x,self.y))
                elif self.is_jump and self.walk_left:
                    window.blit(self.image_jump_left[int((self.jump_count+10)//2.1)],(self.x,self.y))
                elif self.walk_left:
                    window.blit(self.image_walk_left[self.walk_count//3], (self.x, self.y))
                    self.walk_count += 1
                else:
                    window.blit(self.image_walk_right[self.walk_count//3], (self.x, self.y))
                    self.walk_count += 1
            else:
                if keys[pygame.K_SPACE] and  self.walk_right:
                    if shoot_time_delay == 0:
                        window.blit(self.image_shoot_right[0], (self.x, self.y))  
                    else:
                        window.blit(self.image_shoot_right[1], (self.x, self.y))
                elif keys[pygame.K_SPACE] and  self.walk_left:
                    if shoot_time_delay == 0:
                        window.blit(self.image_shoot_left[0], (self.x, self.y))  
                    else:
                        window.blit(self.image_shoot_left[1], (self.x, self.y))
                    
                elif self.walk_left:
                    window.blit(self.image_stand_left, (self.x, self.y))
                else:# self.walk_left and not self.is_jump :
                    window.blit(self.image_stand_right, self.hitbox)
                
            self.hitbox = (self.x + 38, self.y + 15, 66, 90)         
            #pygame.draw.rect(window,(255,0,0),self.hitbox,2)

    def move(self): 
        global keys
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and shoot_time_delay == 0 and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
            self.shooting = True
            if self.walk_left:
                facing = -1
            else:
                facing = 1 

            if len(bullets) < 6:  
                # Once list is a mutable object we can append ellements to it
                bullets.append(projectile((self.x + self.width//2),(self.y + self.height//1.5),facing))
        else:
            self.shooting = False

        if keys[pygame.K_UP] and not self.is_jump and keys[pygame.K_RIGHT]:
            self.stand = False 
            self.walk_right = True
            self.is_jump = True
            self.jump_count = 10
        elif keys[pygame.K_UP] and not self.is_jump and keys[pygame.K_LEFT]:
            self.stand = False 
            self.walk_left = True
            self.is_jump = True
            self.jump_count = 10
        elif keys[pygame.K_UP] and not self.is_jump:
            self.stand = True 
            self.is_jump = True
            self.jump_count = 10
        elif keys[pygame.K_LEFT]:
            self.stand = False
            self.walk_left = True
            self.walk_right = False
            if self.x > 0 :
                self.x -= self.velocity
        elif keys[pygame.K_RIGHT]:
            self.stand = False
            self.walk_left = False
            self.walk_right = True
            if self.x < window_width - 64 :
                self.x += self.velocity           
        else:
            if not self.is_jump:
                self.stand = True
            

        if self.is_jump:     
            self.velocity = 7   
            if self.jump_count > 0:
                self.y = (self.y - (self.jump_count**2)* 0.5)
                self.jump_count -= 1
            elif self.jump_count <= 0 and self.jump_count >= - 10:
                self.y = (self.y + (self.jump_count**2)* 0.5)
                self.jump_count -= 1
            else:
                self.jump_count = 0 
                self.is_jump = False
                self.stand = True
                self.velocity = 5
        self.hitbox = (self.x + 17, self.y + 11, 25, 52 )
    
    def hit(self):
        self.life -= 1
        print('PLAYER HIT')

class Enemy(element):
    
    image_walk_right = [pygame.image.load('Minotaur-Walk(R)(1).png'),pygame.image.load('Minotaur-Walk(R)(2).png'),pygame.image.load('Minotaur-Walk(R)(3).png'),pygame.image.load('Minotaur-Walk(R)(4).png'),pygame.image.load('Minotaur-Walk(R)(5).png'),pygame.image.load('Minotaur-Walk(R)(6).png'),pygame.image.load('Minotaur-Walk(R)(7).png'),pygame.image.load('Minotaur-Walk(R)(8).png'),pygame.image.load('Minotaur-Walk(R)(9).png'),pygame.image.load('Minotaur-Walk(R)(10).png'),pygame.image.load('Minotaur-Walk(R)(11).png'),pygame.image.load('Minotaur-Walk(R)(12).png'),pygame.image.load('Minotaur-Walk(R)(13).png'),pygame.image.load('Minotaur-Walk(R)(14).png'),pygame.image.load('Minotaur-Walk(R)(15).png'),pygame.image.load('Minotaur-Walk(R)(16).png'),pygame.image.load('Minotaur-Walk(R)(17).png'),pygame.image.load('Minotaur-Walk(R)(18).png')]

    image_walk_left = [pygame.image.load('Minotaur-Walk(L)(1).png'),pygame.image.load('Minotaur-Walk(L)(2).png'),pygame.image.load('Minotaur-Walk(L)(3).png'),pygame.image.load('Minotaur-Walk(L)(4).png'),pygame.image.load('Minotaur-Walk(L)(5).png'),pygame.image.load('Minotaur-Walk(L)(6).png'),pygame.image.load('Minotaur-Walk(L)(7).png'),pygame.image.load('Minotaur-Walk(L)(8).png'),pygame.image.load('Minotaur-Walk(L)(9).png'),pygame.image.load('Minotaur-Walk(L)(10).png'),pygame.image.load('Minotaur-Walk(L)(11).png'),pygame.image.load('Minotaur-Walk(L)(12).png'),pygame.image.load('Minotaur-Walk(L)(13).png'),pygame.image.load('Minotaur-Walk(L)(14).png'),pygame.image.load('Minotaur-Walk(L)(15).png'),pygame.image.load('Minotaur-Walk(L)(16).png'),pygame.image.load('Minotaur-Walk(L)(17).png'),pygame.image.load('Minotaur-Walk(L)(18).png')]

    def __init__(self,x):
        element.__init__(self,x,515,128,128,1) # 3

        self.hitbox = (self.x + 25, self.y + 55 ,65,70)
        self.walk_count = 0
        self.walk_right = False
        self.walk_left = True

    def draw(self,window):
        # Once the enemy move autonomus we add the move in draw
        self.move()
        # Each image will be used in 3 frames
        if self.walk_count +1 >= 54:
            self.walk_count = 0
        
        # test if i need the self in image
        if self.walk_left:
            window.blit(self.image_walk_left[self.walk_count//3], (self.x,self.y + self.height/3))
            self.walk_count += 1
            # Given the irregularity of sides
            self.hitbox = (self.x + 25, self.y + 55 ,65,70) 
        elif self.walk_right:
            window.blit(self.image_walk_right[self.walk_count//3], (self.x,self.y + self.height/3))
            self.walk_count += 1

            self.hitbox = (self.x + 34, self.y + 55 ,70,70)
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

    image_bullet_right = pygame.image.load('flying-bulletR.png')
    image_bullet_left = pygame.image.load('flying-bulletL.png')

    def __init__(self,x,y,facing):
        element.__init__(self,x,y,128,128,3) # Player width and Height
        self.hitbox = () # (self.x + 100 ,self.y,64,128)
        # 1 = right, -1 = left
        self.facing = facing

    def draw(self,window): 
        if self.facing == 1:
            window.blit(self.image_bullet_right, (self.x + self.width/1.7 ,self.y - self.height/10)) 
            self.hitbox = (self.x + 115 ,self.y + 7 ,20,10)
        elif self.facing ==  -1:
            window.blit(self.image_bullet_left, (self.x - self.width/1.5,self.y - self.height/10))
            self.hitbox = (self.x - 80,self.y + 7 ,20,10)       
        # pygame.draw.rect(window, (0,0,0), self.hitbox,2)
      
def bullet_interaction(bullets):
    '''Update the bullets list in hit case and invoke enemy.hit() '''
  
    for bullet in bullets:
        
        for enemy in enemies:
            if (enemy.hitbox[0] < (bullet.hitbox[0]+bullet.hitbox[2]/2) < (enemy.hitbox[0] + enemy.hitbox[2])) and( enemy.hitbox[1]< (bullet.hitbox[1]+bullet.hitbox[3]/2) < (enemy.hitbox[1] + enemy.hitbox[3])):
                enemy.hit()
                if bullet in bullets: # If used to prevent error in the bullet removal    
                    bullets.pop(bullets.index(bullet))
            
            
        if bullet.x < 0 or bullet.x > window_width:
            try:
                bullets.pop(bullets.index(bullet))
            except ValueError:
                bullets.clear()
        else:
            bullet.x = bullet.x + bullet.facing * bullet.velocity


def enemy_player_collision():
    for enemy in enemies:
        if (player.hitbox[1] + player.hitbox[2]) > enemy.hitbox[1]:
            
            if enemy.hitbox[0]< player.hitbox[0] < (enemy.hitbox[0] + enemy.hitbox[2]):
                player.hit()
            elif enemy.hitbox[0] < (player.hitbox[0] + player.hitbox[2]) < (enemy.hitbox[0] + enemy.hitbox[2]):
                player.hit()

def redraw_game_window(player,bullets,enemies,window): 
    # Add the background
    window.blit(background, (0,0))
    # Add the player
    player.draw(window)

    [bullet.draw(window) for bullet in bullets]
    [enemy.draw(window) for enemy in enemies]
    pygame.display.update()

clock = pygame.time.Clock()
window_width = 1229
window_hight = 691
game_window = pygame.display.set_mode((window_width,window_hight))
background = pygame.image.load('old_town (Custom).jpg')

player = Player()
bullets=[]
prog_run = True

enemies = []
enemies.append(Enemy(300)) # Enemy initial position
enemies.append(Enemy(100))

# Game main loop


shoot_time_delay = 0
while prog_run:
    clock.tick(27) # Make the fresh rate lower than 27 fps 
    for event in pygame.event.get():
    # QUIT means the 'X' that we normally close windows in the right upper corner
        if event.type == pygame.QUIT: 
            prog_run = False
    
    if shoot_time_delay > 10:
        shoot_time_delay = 0
    else:
        shoot_time_delay += 1
    # Collisions
    bullet_interaction(bullets)
    enemy_player_collision()
    player.move()
    redraw_game_window(player,bullets,enemies,game_window)
                


                



