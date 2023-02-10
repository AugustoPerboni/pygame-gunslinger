from gunslinger_package.config import *
from gunslinger_package.loaded_images.brown_minotaur_images import *

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
                bullets.pop(bullets.index(bullet))
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

def redraw_game_window(background,player,bullets,enemies,window): 
    '''Draw all the game_window elements.'''

    # Add the background
    window.blit(background, (0,0))
    # Add the player
    player.draw(window)

    [bullet.draw(window) for bullet in bullets]
    [enemy.draw(window,brown_minotaur_image_walk_left,brown_minotaur_image_walk_right) for enemy in enemies if enemy.name == 'brown_minotaur']

    pygame.display.update()