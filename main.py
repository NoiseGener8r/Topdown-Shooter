## TODO ##

# Fix enemy hitboxes
# No enemies near player spawn
# 

# Topdown Shooter
# By NoiseGenerator
# Licensed under GNU GPL

import pygame, random, math, sys
from pygame.math import Vector2
pygame.init()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
item_list = pygame.sprite.Group()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


pygame.init()

# Set the height and width of the screen
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Topdown")

# Images:
player_up = pygame.image.load('./images/player_up.png').convert_alpha()
player_right = pygame.transform.rotate(player_up, -90)
player_left = pygame.transform.rotate(player_up, 90)
player_down = pygame.transform.rotate(player_up, 180)

ammo_pile = pygame.image.load('./images/ammo_pile.png').convert_alpha()
health_pickup = pygame.image.load('./images/health_pickup.png').convert_alpha()    

foe_image = pygame.image.load('./images/foe.png').convert_alpha()

# OTHER CONSTANTS

RANDOMNESS = 500

class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
        self.original_image = player_up
        self.image = player_up
        
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.new_x = 0
        self.new_y = 0
        
        self.hp = 10
        self.ammo = 50
        self.score = 0
        
        self.weapon = 1
        self.invincibility = 0
        
    def update(self):
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > SCREEN_WIDTH - player.rect.width:
            self.rect.x = SCREEN_WIDTH - player.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > SCREEN_HEIGHT - player.rect.height:
            self.rect.y = SCREEN_HEIGHT - player.rect.height
        self.rect.x += self.new_x      
        self.rect.y += self.new_y
        self.invincibility -= 1
        
        
        
        
    def up(self):
        
        self.new_y = -4
        self.image = player_up
    def down(self):
        
        self.new_y = 4
        self.image = player_down
    def left(self):
        
        self.new_x = -4
        self.image = player_left
    def right(self):
        
        self.new_x = 4
        self.image = player_right
        
    def stop(self):
        
        self.new_x = 0
        self.new_y = 0
            
    
    
   
                
        
class Enemy(pygame.sprite.Sprite):
    """ This class represents the enemy . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = foe_image
        
        
        self.rect = self.image.get_rect()
              
        
    def update(self):
        global player
        if self.rect.center[0] != player.rect.center[0] or self.rect.center[1] != player.rect.center[1]:
            # find normalized direction vector (dx, dy) between enemy and player
            dx, dy = self.rect.center[0] - player.rect.center[0], self.rect.center[1] - player.rect.center[1]
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist
            # move along this normalized vector towards the player at current speed
            self.rect.x -= dx * 3
            self.rect.y -= dy * 3   
            angle = math.degrees(math.atan2(dy, dx))
            if angle < 0:
                angle += 360
            self.image = pygame.transform.rotate(foe_image, -angle+90)
        
              
        
        
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self, x, y, angle, speed):
        
        
        pygame.sprite.Sprite.__init__(self)
        # Rotate the bullet image (negative angle because y-axis is flipped).
        self.image = pygame.transform.rotate(pygame.Surface([5,5]), angle)
        self.rect = self.image.get_rect(center=(x, y))
        angle = math.radians(angle)
        
        self.speed_x = speed * math.cos(angle)
        self.speed_y = speed * math.sin(angle)       
               
        
        
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
class Item(pygame.sprite.Sprite):
    """This is the generic item class all other items are derived from . """
    def __init__(self):
        
        super().__init__()
        
            
        
class AmmoPile(Item):
    """This is the ammo pickup . """
    def __init__(self):
        
        super().__init__()
        
        self.image = ammo_pile
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        
    def pickup(self):
        player.ammo += 10
        
class Heart(Item):
    """This is the health pickup . """
    def __init__(self):
        
        super().__init__()
        
        self.image = health_pickup
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = random.randint(0, SCREEN_HEIGHT)
        
    def pickup(self):
        player.hp += 1
        
        
def drawtext(screen, text, color, x, y):  
    pygame.font.init() # you have to call this at the start, 
                # if you want to use this module.
    myfont = pygame.font.SysFont('Press Start 2P', 40)  
    newtextsurface = myfont.render(str(text), False, color)
    screen.blit(newtextsurface, (x, y))
    
def create_item(item_id):
    
    if item_id > 0 and item_id < 2:
        ammo_pile = AmmoPile()
        all_sprites_list.add(ammo_pile)
        item_list.add(ammo_pile)   
    if item_id == 1:
        heart = Heart()
        all_sprites_list.add(heart)
        item_list.add(heart)
    else:
        return 0
    

def main():
    global player
    """ Main Program """
    
    
    # Create the player
    player = Player()   
    
    
    

    player.rect.x = 340
    player.rect.y = 300
    all_sprites_list.add(player)   
    

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
    key = pygame.key.get_pressed()
    main_menu = True
    
    if main_menu:
        screen.fill(BLACK) 
        drawtext(screen, 'TOPDOWN SHOOTER', RED, 25, 25)
        drawtext(screen, 'BY NOISEGENERATOR', RED, 25, 60)
        drawtext(screen, 'PRESS ENTER TO BEGIN...', RED, 25, 565)
         
        pygame.display.flip()
    while main_menu:
        try:
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
            
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = False
                        main_menu = False
        except:
            pygame.quit()
            sys.exit()
        
    # -------- Main Program Loop -----------
    while not done and not main_menu:
        key = pygame.key.get_pressed()
        
        

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                done = True
                # MOVEMENT #
                
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                   
                    if player.weapon == 1 and player.ammo > 0:
                       
                        vector_x = pygame.mouse.get_pos()[0] - player.rect.center[0]
                        vector_y = pygame.mouse.get_pos()[1] - player.rect.center[1]
                        vector = math.hypot(vector_x, vector_y)
                        angle = math.degrees(math.atan2(vector_y, vector_x))
                        if angle < 0:
                            angle += 360
                        bullet = Bullet(player.rect.center[0], player.rect.center[1], angle, 6)
                        bullet_list.add(bullet)
                        all_sprites_list.add(bullet)
                        player.image = pygame.transform.rotate(player_up, -angle-90)
                        player.ammo -= 1 
                        
                    if player.weapon == 2 and player.ammo > 2:
                        
                        vector_x = pygame.mouse.get_pos()[0] - player.rect.center[0]
                        vector_y = pygame.mouse.get_pos()[1] - player.rect.center[1]
                        vector = math.hypot(vector_x, vector_y)
                        angle = math.degrees(math.atan2(vector_y, vector_x))
                        if angle < 0:
                            angle += 360
                        for i in range(3):
                            bullet = Bullet(player.rect.center[0], player.rect.center[1], angle-10, 6)
                            bullet_list.add(bullet)
                            all_sprites_list.add(bullet)
                            bullet = Bullet(player.rect.center[0], player.rect.center[1], angle, 6)
                            bullet_list.add(bullet)
                            all_sprites_list.add(bullet)
                            bullet = Bullet(player.rect.center[0], player.rect.center[1], angle+10, 6)
                            bullet_list.add(bullet)
                            all_sprites_list.add(bullet)                        
                        player.image = pygame.transform.rotate(player_up, -angle-90)
                        player.ammo -= 3
                        
                if event.key == pygame.K_3:
                    player.weapon = 2
                if event.key == pygame.K_2:
                    player.weapon = 0
                if event.key == pygame.K_1:
                    player.weapon = 1
                    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        if player.weapon < 2:
                            player.weapon += 1
                        else:
                            player.weapon = 0
                    elif event.button == 5:
                        if player.weapon > 0:
                            player.weapon -= 1
                        else:
                            player.weapon = 2
                        
            
                    
                    # FIRING #
          #checking pressed keys
       
        if key[pygame.K_w]:
            player.up()
        if key[pygame.K_s]:
            player.down()
        if key[pygame.K_a]:
            player.left()
        if key[pygame.K_d]:
            player.right()
        
        if not key[pygame.K_w] and not key[pygame.K_a] and not key[pygame.K_s] and not key[pygame.K_d]:
            player.stop()
            
        
            
        if player.weapon == 0 and player.ammo > 0:
            if key[pygame.K_SPACE]:
                
                vector_x = pygame.mouse.get_pos()[0] - player.rect.center[0]
                vector_y = pygame.mouse.get_pos()[1] - player.rect.center[1]
                vector = math.hypot(vector_x, vector_y)
                angle = math.degrees(math.atan2(vector_y, vector_x))
                if angle < 0:
                    angle += 360
                bullet = Bullet(player.rect.center[0], player.rect.center[1], angle, 6)
                bullet_list.add(bullet)
                all_sprites_list.add(bullet)
                player.image = pygame.transform.rotate(player_up, -angle-90)
                player.ammo -= 1
                
        
                                    
            
        
                   
        
        enemy_spawn_chance = random.randint(0, RANDOMNESS)
        
        if enemy_spawn_chance <= 10:
            # This represents a enemy
            
            enemy = Enemy()  
            enemy_spawn = random.randint(0,3)
            if enemy_spawn == 0:
                
                enemy.rect.y = random.randint(0,SCREEN_HEIGHT)
                enemy.rect.x = -10
                
            if enemy_spawn == 1:
                
                enemy.rect.y = random.randint(0,SCREEN_HEIGHT)
                enemy.rect.x = SCREEN_WIDTH
                
            if enemy_spawn == 2:
                
                enemy.rect.x = random.randint(0,SCREEN_WIDTH)
                enemy.rect.y = -10
                
            if enemy_spawn == 3:
                
                enemy.rect.x = random.randint(0,SCREEN_WIDTH)
                enemy.rect.y = SCREEN_HEIGHT
         
            # Add the enemy to the list of objects
            enemy_list.add(enemy)
            all_sprites_list.add(enemy)  
            
        
            


        all_sprites_list.update() 
        # Calculate mechanics for each bullet
        for bullet in bullet_list:
    
            # See if it hit a block
            enemy_hit_list = pygame.sprite.spritecollide(bullet, enemy_list, True)
    
            # For each block hit, remove the bullet and add to the score
            for enemy in enemy_hit_list:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)
                player.score += 1
                #print(score)
    
            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10 or bullet.rect.y > SCREEN_HEIGHT or bullet.rect.x > SCREEN_WIDTH or bullet.rect.x < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)  
                
        
        for enemy in enemy_list:
    
            
            player_hit_list = pygame.sprite.spritecollide(player, enemy_list, True)
    
            if player.invincibility < 0:
                for enemy in player_hit_list:
                    enemy_list.remove(enemy)
                    all_sprites_list.remove(enemy)
                    player.hp -= 1
                    player.invincibility = 50
                    
                
                
                
        
        pickup_chance = random.randint(0,RANDOMNESS)
        create_item(pickup_chance)
            
    

        for item in item_list:
    
           
            item_pickup_list = pygame.sprite.spritecollide(player, item_list, True)
    
            
            for item in item_pickup_list:
                item.pickup()
                item_list.remove(item)
                all_sprites_list.remove(item)
                
                    
        if player.hp <= 0:
            
            done = True
        for i in range(20):
            pygame.time.Clock()
            current_fps =  pygame.time.Clock().get_fps()
            
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.fill((255, 205, 102))
        
        all_sprites_list.draw(screen)
        drawtext(screen, 'Ammo: ' + str(player.ammo), RED, 130, 10)
        drawtext(screen, 'HP: ' + str(player.hp), RED, 10, 10)
        drawtext(screen, 'Score: ' + str(player.score), RED, SCREEN_WIDTH-150, 10)
        if player.weapon == 0:
            drawtext(screen, 'Weapon: SMG', RED, SCREEN_WIDTH-400, 10)
        if player.weapon == 1:
            drawtext(screen, 'Weapon: USP', RED, SCREEN_WIDTH-400, 10)
        if player.weapon == 2:
            drawtext(screen, 'Weapon: Shotgun', RED, SCREEN_WIDTH-400, 10)
            
        drawtext(screen, str(current_fps), RED, SCREEN_WIDTH-100, SCREEN_HEIGHT-50)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    
    if done and not main_menu: 
        screen.fill(BLACK)
        drawtext(screen, 'GAME OVER', RED, 310, 210)
        drawtext(screen, 'SCORE: ' + str(player.score), RED, 310, 310)        
        pygame.display.flip()
    
    while done and not main_menu:   
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() 
                    sys.exit()
        except:
            pygame.quit()
            sys.exit()
            
    pygame.quit()
    sys.exit()
    
    
    
if __name__ == "__main__":
    main()
