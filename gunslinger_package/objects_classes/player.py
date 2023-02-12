import sys
sys.path.append('C:\\Users\\augus\\Desktop\\gunslinger-division')

from gunslinger_package.config import *
from gunslinger_package.objects_classes.element import Element
from gunslinger_package.objects_classes.projectile import Projectile
from gunslinger_package.loaded_images.player_images import *
from gunslinger_package.objects_classes.turret import Turret
from gunslinger_package.functions import turret_insert_index

class Player(Element):

    def __init__(self):
        Element.__init__(self,50,525,64,64,5,30)

        self.hitbox = (self.x + 38, self.y + 15, 66, 90)
        self.jump_count = 0
        self.is_jump = False 
        self.dead_count = 0
        self.turret_count = 0
        
        self.stand = True
        self.walk_left = False
        self.walk_right = False
        self.walk_count = 0
        self.shooting = False
        self.shoot_time_delay = 0
        self.life_bar_x = 66
        self.life_bar_y = 525
        self.money = 100


    def draw(self,window,keys):
        
        if self.life <= 0:
            if self.dead_count + 1 <= 24 and self.walk_right:
                window.blit(player_image_dead_right[self.dead_count//3],(self.x,self.y))
                self.dead_count += 1    
            elif self.dead_count + 1 <= 24 and self.walk_left:
                window.blit(player_image_dead_left[self.dead_count//3],(self.x,self.y))
                self.dead_count += 1             
            else:
                quit()
        else:
            self.life_bar_x = self.x + self.width/2.7
            self.life_bar_y = self.y 
            self.life_bar(window)

            if self.walk_count + 1 >= 21:
                    self.walk_count = 0

            if not self.stand:        
                if self.is_jump and self.walk_right:
                    window.blit(player_image_jump_right[int((self.jump_count+10)//2.1)],(self.x,self.y))
                elif self.is_jump and self.walk_left:
                    window.blit(player_image_jump_left[int((self.jump_count+10)//2.1)],(self.x,self.y))
                elif self.walk_left:
                    window.blit(player_image_walk_left[self.walk_count//3], (self.x, self.y))
                    self.walk_count += 1
                else:
                    window.blit(player_image_walk_right[self.walk_count//3], (self.x, self.y))
                    self.walk_count += 1
            else:
                if keys[pygame.K_SPACE] and  self.walk_right:
                    if self.shoot_time_delay == 0:
                        window.blit(player_image_shoot_right[0], (self.x, self.y))  
                    else:
                        window.blit(player_image_shoot_right[1], (self.x, self.y))
                elif keys[pygame.K_SPACE] and  self.walk_left:
                    if self.shoot_time_delay == 0:
                        window.blit(player_image_shoot_left[0], (self.x, self.y))  
                    else:
                        window.blit(player_image_shoot_left[1], (self.x, self.y))
                    
                elif self.walk_left:
                    window.blit(player_image_stand_left, (self.x, self.y))
                else:# self.walk_left and not self.is_jump :
                    window.blit(player_image_stand_right, self.hitbox)
                
            self.hitbox = (self.x + 38, self.y + 15, 66, 90)         
            #pygame.draw.rect(window,(255,0,0),self.hitbox,2)

    def move(self,bullets,turrets,keys): 
        ''' 
            Responsible for all the player moves and actions.
        
            Appends bullet to the list bullets
        '''
        # Shoot time delay counter
        if self.shoot_time_delay > 10:
            self.shoot_time_delay = 0
        else:
            self.shoot_time_delay += 1

        
        if self.turret_count >= 50:
            self.turret_count = 0
        elif self.turret_count == 0:
            pass
        else:
            self.turret_count += 1

        if keys[pygame.K_t] and self.turret_count == 0 and self.money >= 100: 
            
            turrets.append(Turret(self.x))
            self.turret_count = 1
            self.money -= 100

        if keys[pygame.K_SPACE] and self.shoot_time_delay == 0 and not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_UP]:
            self.shooting = True
            if self.walk_left:
                facing = -1
            else:
                facing = 1 

            if len(bullets) < 6:  
                # Once list is a mutable object we can append ellements to it
                bullets.append(Projectile((self.x + self.width//2),(self.y + self.height//1.5),facing))
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
            # if self.x < window_width - 64 :
            #     self.x += self.velocity  
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
    
    def hit(self, damage):
        self.life -= damage
        # print('PLAYER HIT')