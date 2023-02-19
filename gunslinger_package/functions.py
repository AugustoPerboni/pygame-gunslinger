import pygame
from random import randint

import sys
sys.path.append('C:\\Users\\augus\\Desktop\\gunslinger-division')

from gunslinger_package.loaded_images.menu_images import *
from gunslinger_package.config import *
from gunslinger_package.objects_classes.enemy import Enemy
from gunslinger_package.loaded_images.brown_minotaur_images import brown_minotaur_images



def bullet_interaction(bullets,enemies,bullet_power,origin_background):
    '''Update the bullet position, the list and in hit case and call enemy.hit() '''
  
    for bullet in bullets:
        
        for enemy in enemies:      
            if collide(enemy, bullet):
                enemy.hit(bullet_power)
                if bullet in bullets: # If used to prevent error in the bullet removal    
                    bullets.pop(bullets.index(bullet))
         
        if bullet.x < origin_background[0] or (bullet.x - origin_background[0]) > (2 * window_width):
            try:
                del bullets[bullets.index(bullet)]
            except ValueError:
                bullets.clear()
        else:
            bullet.x = bullet.x + bullet.facing * bullet.velocity

def enemy_player_collision(enemies,player):
    ''' Calls player.hit if the player collide with an enemy.'''

    for enemy in enemies:
        if collide(player,enemy):
                player.hit(enemy.power)
  
def redraw_game_window(background,player,bullets,enemies,window,end_of_screen,origin_background,turrets,keys,font): 
    '''Draw all the game_window elements.'''

    # Update the background and all the elements when the player reachs the end of the screen
    if ((end_of_screen - player.x) < (50) ) and (origin_background[0] >= 0):
        origin_background = (-window_width,0)
        player.x = 55
        for enemy in enemies:
            enemy.x -= window_width
        for bullet in bullets:
            bullet.x -= window_width
            # Once the turret don't move, the hitbox and life_bar_x are updated now to prevent unecessary conditions in the draw function
        for turret in turrets:
            turret.x -= window_width
            turret.hitbox = (turret.x,turret.y,100,90)
            turret.life_bar_x = turret.x
        #end_of_screen = 2*window_width
    elif (origin_background[0] < 0) and ( player.x < 50 ):
        origin_background = (0,0)
        for enemy in enemies:
            enemy.x += window_width
        for bullet in bullets:
            bullet.x += window_width
        for turret in turrets:
            turret.x += window_width
            turret.hitbox = (turret.x,turret.y,100,90)
            turret.life_bar_x = turret.x
        player.x = 1100    

    window.blit(background,origin_background)
    show_money(player,window)
    
    
    # Update the image of bullets
    [bullet.draw(window) for bullet in bullets]
    # Update the enemy images
    [enemy.draw(window,enemy,enemies,origin_background,player) for enemy in enemies if enemy.name == 'brown_minotaur']

    
    # Draw all the turrets and turrets bullets
    for turret in turrets:
        turret.draw(window,turrets,enemies)
        turret.shoot(enemies)
        for bullet in turret.bullets:
            bullet.draw(window)

    # Draw player in the end to be infront of all the other objects 
    player.draw(window,keys)
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

def enemy_turret_collision(enemies,turrets):
    '''Change the is_hitting value in case of collision and call turret.hit() on the right animation time.'''

    for turret in turrets: 
        for enemy in enemies:
            if collide(turret,enemy):
                enemy.is_hitting = True
                if enemy.hitting_count == 24:
                    turret.hit(enemy.power)
    
def turret_insert_index(turrets,x):
    ''' Return the index of the element before of the desire position.
        The turrents list is sorted by position x in descending order 
    '''
    if len(turrets) == 0:
        return 0
    else:
        for turret in turrets:
            if x > turret.x:
                return(turrets.index(turret)-1)
        else:
            return len(turrets)
                
def show_money(player,window):
    ''' Print in the game window the total money of the player'''
    #window.blit(barra_coin,(window_width-195,15))
    font = create_font(45)
    text = font.render(str(player.money) ,1,(255,255,0))
    window.blit(text,(window_width - 100, 25))
    window.blit(coin_image,(window_width-160,25))
    
def mouse_turret_upgrade(turrets,player,window):
    ''' Check if the cursor is over the turret to print the turret update menu 
        option.
    '''
    for turret in turrets:
        if is_cursor_over(turret):
            turret.draw_menu_update(window,30,player)

def create_font(font_size):
    ''' Create a font with a given font size'''
    return pygame.font.SysFont("Times New Roman", font_size, True)

def collide(element_1,element_2):
    ''' Check if the two elements' hitbox collides. '''

    if ( element_2.hitbox[0] < (element_1.hitbox[0] + element_1.hitbox[2]) < (element_2.hitbox[0] + element_2.hitbox[2]) ) or ( element_1.hitbox[0] < (element_2.hitbox[0] + element_2.hitbox[2]) < (element_1.hitbox[0] + element_1.hitbox[2]) ):
        if (element_2.hitbox[1] < element_1.hitbox[1] + element_1.hitbox[3]):
            return True
    else:
        return False
    
def is_cursor_over(element):
    ''' Check if the mouse cursor is inside the element hitbox.'''
    cursor_x, cursor_y = pygame.mouse.get_pos()
    if element.hitbox[0] < cursor_x < element.hitbox[0] + element.hitbox[2]:
        if element.hitbox[1] < cursor_y < element.hitbox[1] + element.hitbox[3]:
            return True
    else:
        return False