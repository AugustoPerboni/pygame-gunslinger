import sys
sys.path.append('C:\\Users\\augus\\Desktop\\gunslinger-division')

from gunslinger_package.objects_classes.element import Element
from gunslinger_package.config import window_width

class Enemy(Element):
    ''' Define the game enemies. '''

    def __init__(self,x,speed,power,name):
        Element.__init__(self,x,515,128,128,speed,power) # 3

        self.hitbox = (self.x + 25, self.y + 55 ,65,70)
        self.walk_count = 0
        self.walk_right = False
        self.walk_left = True
        self.dead_count = 0
        # Used to differentiate each kind of enemy 
        self.name = name

    def draw(self,window,img_walk_left,img_walk_right):

        # if self.life <= 0:
        #     if self.dead_count + 1 <= 24:
        #         window.blit(self.image_dead_right[self.dead_count//3],(self.x,self.y))
        #         self.dead_count += 1       

        # Once the enemy move autonomus we add the move in draw
        self.move()
        self.life_bar(window)
        # Each image will be used in 3 frames
        if self.walk_count +1 >= 54:
            self.walk_count = 0
        
        # test if i need the self in image
        if self.walk_left:
            window.blit(img_walk_left[self.walk_count//3], (self.x,self.y + self.height/3))
            self.walk_count += 1
            # Given the irregularity of sides
            self.hitbox = (self.x + 25, self.y + 55 ,65,70) 
        elif self.walk_right:
            window.blit(img_walk_right[self.walk_count//3], (self.x,self.y + self.height/3))
            self.walk_count += 1

            self.hitbox = (self.x + 34, self.y + 55 ,70,70)
        # pygame.draw.rect(window,(255,0,0), self.hitbox,2)
    def hit(self,damage):
        print('ENEMY HIT')
        self.life -= damage

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