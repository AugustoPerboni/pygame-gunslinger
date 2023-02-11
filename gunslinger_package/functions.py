import pygame

from random import randint
import sys
sys.path.append('C:\\Users\\augus\\Desktop\\gunslinger-division')

from gunslinger_package.config import *
from gunslinger_package.objects_classes.enemy import Enemy
from gunslinger_package.loaded_images.brown_minotaur_images import brown_minotaur_images




def bullet_interaction(bullets,enemies,player_power):
    '''Update the bullet position, the list and in hit case and call enemy.hit() '''
  
    for bullet in bullets:
        
        for enemy in enemies:
            if (enemy.hitbox[0] < (bullet.hitbox[0]+bullet.hitbox[2]/2) < (enemy.hitbox[0] + enemy.hitbox[2])) and( enemy.hitbox[1]< (bullet.hitbox[1]+bullet.hitbox[3]/2) < (enemy.hitbox[1] + enemy.hitbox[3])):
                enemy.hit(player_power)
                if bullet in bullets: # If used to prevent error in the bullet removal    
                    bullets.pop(bullets.index(bullet))
         
        if bullet.x < 0 or bullet.x > window_width:
            try:
                del bullets[bullets.index(bullet)]
            except ValueError:
                bullets.clear()
        else:
            bullet.x = bullet.x + bullet.facing * bullet.velocity

def enemy_player_collision(enemies,player):
    ''' Calls player.hit if the player collide with an enemy.'''

    for enemy in enemies:
        if (player.hitbox[1] + player.hitbox[2]) > enemy.hitbox[1]:
            
            if enemy.hitbox[0]< player.hitbox[0] < (enemy.hitbox[0] + enemy.hitbox[2]):
                player.hit(enemy.power)
            elif enemy.hitbox[0] < (player.hitbox[0] + player.hitbox[2]) < (enemy.hitbox[0] + enemy.hitbox[2]):
                player.hit(enemy.power)

def redraw_game_window(background,player,bullets,enemies,window,end_of_screen,origin_background): 
    '''Draw all the game_window elements.'''
    # Add the background
    if ((end_of_screen - player.x) < (50) ) and (origin_background[0] >= 0):
        origin_background = (-window_width,0)
        player.x = 55
        for enemy in enemies:
            enemy.x -= window_width
        #end_of_screen = 2*window_width
    elif (origin_background[0] < 0) and ( player.x < 50 ):
        origin_background = (0,0)
        for enemy in enemies:
            enemy.x += window_width
        player.x = 1100    
    window.blit(background,origin_background)
    # Add the player
    player.draw(window)

    [bullet.draw(window) for bullet in bullets]
    [enemy.draw(window,enemy,enemies,origin_background) for enemy in enemies if enemy.name == 'brown_minotaur']

    pygame.display.update()
    return origin_background

def wave_generator(enemies,wave_number):

    # Each speed point represents 55.86 pixel/s
    # One speed point takes 22 seconds to cross the game window
    i = 0
    for i in range((wave_number + 2)**2):
        x = randint(window_width, window_width*(wave_number))
        speed = randint(1,wave_number*2)
        power = randint(1,wave_number*2)
        enemies.append(Enemy(x,speed,power,brown_minotaur_images,'brown_minotaur'))

