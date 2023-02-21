from gunslinger_package.loaded_images.brown_minotaur_images import brown_minotaur_images
from gunslinger_package.objects_classes.enemy import Enemy
from gunslinger_package.config import *
from gunslinger_package.loaded_images.menu_images import *
import pygame
from random import randint, uniform

import sys
sys.path.append(
    'C:\\Users\\augus\\Desktop\\pythonScripts\\General\\myProjects\\gunslinger-division')


def bullet_interaction(bullets, enemies, bullet_power, origin_background, player):
    '''Update the bullet position, the list and in hit case and call enemy.hit() '''

    for bullet in bullets:
        for enemy in enemies:
            if collide(bullet, enemy):
                enemy.hit(bullet_power)

                if bullet in bullets:  # If used to prevent error in the bullet removal
                    bullets.pop(bullets.index(bullet))

        if (player.in_window_second_half and bullet.x > window_width - 135) or (not player.in_window_second_half and bullet.x > 2*window_width):
            try:
                del bullets[bullets.index(bullet)]
            except ValueError:
                bullets.clear()
        else:
            bullet.x = bullet.x + bullet.facing * bullet.velocity


def enemy_player_collision(enemies, player):
    ''' Calls player.hit if the player collide with an enemy.'''

    for enemy in enemies:
        if collide(player, enemy):
            player.hit(enemy.power)


def redraw_game_window(background, player, enemies, window, end_of_screen, origin_background, turrets, keys, font, wave_number):
    '''Draw all the game_window elements.'''

    # Update the background and all the elements when the player reachs the end of the screen

    if ((end_of_screen - player.x) < (50)) and (origin_background[0] >= 0):
        origin_background = (-window_width, 0)
        # Player ----------------------------------------------------#
        player.in_window_second_half = True
        player.window_half_correction()
        # Enemies ---------------------------------------------------#
        for enemy in enemies:
            enemy.window_half_correction(player)
        # Turret ----------------------------------------------------#
        for turret in turrets:
            turret.window_half_correction(player)

    elif (origin_background[0] < 0) and (player.x < 50):
        # Player ----------------------------------------------------#
        player.in_window_second_half = False
        origin_background = (0, 0)
        player.window_half_correction()
        # Enemies ---------------------------------------------------#
        for enemy in enemies:
            enemy.window_half_correction(player)
         # Turret ---------------------------------------------------#
        for turret in turrets:
            turret.window_half_correction(player)

    window.blit(background, origin_background)
    text = font.render('Wave:' + str(wave_number), 1, (0, 0, 0))
    window.blit(text, (525, 10))
    show_money(player, window)

    # Update the image of bullets
    [bullet.draw(window, player) for bullet in player.bullets]
    # Update the enemy images
    [enemy.draw(window, enemy, enemies, origin_background, player)
     for enemy in enemies if enemy.name == 'brown_minotaur']

    # Draw all the turrets and turrets bullets
    for turret in turrets:
        turret.draw(window, turrets, enemies)
        turret.shoot(enemies)
        for bullet in turret.bullets:
            bullet.draw(window, player)

    # Draw player in the end to be infront of all the other objects
    player.draw(window, keys)
    return origin_background


def wave_generator(enemies, wave_number):
    # Each speed point represents 55.86 pixel/s
    # One speed point takes 22 seconds to cross the game window
    i = 0
    for i in range((wave_number + 2)**2):
        x = uniform(window_width*2, window_width *
                    2 + (wave_number/2)*window_width)
        speed = randint(1, wave_number*2)
        power = randint(1, wave_number*2)
        max_life = 20 + wave_number * 10
        enemies.append(
            Enemy(x, speed, power, brown_minotaur_images, 'brown_minotaur', max_life))


def enemy_turret_collision(enemies, turrets):
    '''Change the is_hitting value in case of collision and call turret.hit() on the right animation time.'''

    for turret in turrets:
        for enemy in enemies:
            if collide(turret, enemy):
                enemy.is_hitting = True
                if enemy.hitting_count == 24:
                    turret.hit(enemy.power)
                    if turret.life <= 0:
                        enemy.is_hitting = False


def turret_insert_index(turrets, x):
    ''' Return the index of the element before of the desire position.
        The turrents list is sorted by position x in descending order 
    '''
    if len(turrets) == 0:
        return 0
    else:
        for turret in turrets:
            if x > turret.x:
                return (turrets.index(turret)-1)
        else:
            return len(turrets)


def show_money(player, window):
    ''' Print in the game window the total money of the player'''
    # window.blit(barra_coin,(window_width-195,15))
    font = create_font(45)
    text = font.render(str(player.money), 1, (255, 255, 0))
    window.blit(text, (window_width - 100, 25))
    window.blit(coin_image, (window_width-160, 25))


def turret_menu_interaction(turrets, player, window, menu):
    ''' Call the method interaction for each turret, using the same menu swaping the characteristics. '''

    for turret in turrets:
        if is_cursor_over(turret):
            menu.interaction(turret, window, player)


def create_font(font_size):
    ''' Create a font with a given font size'''
    return pygame.font.SysFont("Times New Roman", font_size, True)


def collide(element_1, element_2):
    ''' Check if the two elements' hitbox collides. '''

    if (element_2.hitbox[0] < (element_1.hitbox[0] + element_1.hitbox[2]) < (element_2.hitbox[0] + element_2.hitbox[2])) or (element_1.hitbox[0] < (element_2.hitbox[0] + element_2.hitbox[2]) < (element_1.hitbox[0] + element_1.hitbox[2])):
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
