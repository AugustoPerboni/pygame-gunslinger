import pygame
class Element:
    ''' Basic build block of the game elements.'''

    def __init__(self,x,y,width,height,velocity,power):
        ''' Shared attributes of our characters in game.'''
        self.x = x
        self.y = y 
        self.width = width
        self.height = height
        self.velocity = velocity
        self.power = power
        self.hitbox = ()
        self.life = 100
        self.life_color = ()
        #self.life_bar_x = life_bar_x
        # self.life_bar_y = life_bar_y

    def life_bar(self,window):
        ''' Find the respective color for the life value in the color scale.'''
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
        pygame.draw.rect(window,(0,0,0),(self.life_bar_x,self.life_bar_y,100,10),2)
        pygame.draw.rect(window,self.life_color,(self.life_bar_x,self.life_bar_y,self.life,10))
        