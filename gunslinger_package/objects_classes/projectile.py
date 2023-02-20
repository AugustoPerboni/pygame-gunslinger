import sys
sys.path.append('C:\\Users\\augus\\Desktop\\pythonScripts\\General\\myProjects\\gunslinger-division')

from gunslinger_package.loaded_images.effects_images import image_bullet_left,image_bullet_right
from gunslinger_package.objects_classes.element import Element
from gunslinger_package.config import *


class Projectile(Element):

    def __init__(self,x,y,facing):
        Element.__init__(self,x,y,128,128,20,1 ) # Player width and Height
        self.hitbox = () # (self.x + 100 ,self.y,64,128)
        # 1 = right, -1 = left
        self.facing = facing

    def draw(self,window,player):
        if player.in_window_second_half and self.x > window_width or not player.in_window_second_half and self.x < window_width:   
            if self.facing == 1:
                window.blit(image_bullet_right, (self.x + self.width/1.7 ,self.y - self.height/10)) 
                self.hitbox = (self.x + 115 ,self.y + 7 ,20,10)
            elif self.facing ==  -1:
                window.blit(image_bullet_left, (self.x - self.width/1.5,self.y - self.height/10))
                self.hitbox = (self.x - 80,self.y + 7 ,20,10)       
            # pygame.draw.rect(window, (0,0,0), self.hitbox,2)

        