## TODO ##

# Continue making bullets go pew pew

# Topdown Shooter
# By NoiseGenerator
# Licensed under GNU GPL

import pygame, random, math
from pygame.math import Vector2
pygame.init()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Images:
player_image_right = pygame.image.load('player_right.png')
player_image_left = pygame.image.load('player_left.png')
player_image_up = pygame.image.load('player_right.png')
player_image_down = pygame.image.load('player_left.png')


class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
        controls. """
 
    # -- Methods
    def __init__(self):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
                
        self.image = player_image_right
        
        self.rect = self.image.get_rect()
 
        # Set speed vector of player
        self.new_x = 0
        self.new_y = 0
        
    def update(self):
        """ Move the player. """
        
        self.rect.x += self.new_x      
        self.rect.y += self.new_y
        
        
    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.new_x = -3
        self.image = player_image_left  
    def go_right(self):
        """ Called when the user hits the left arrow. """
        self.new_x = 3
        self.image = player_image_right 
    def go_up(self):
        """ Called when the user hits the left arrow. """
        self.new_y = -3
        self.image = player_image_up 
    def go_down(self):
        """ Called when the user hits the left arrow. """
        self.new_y = 3
        self.image = player_image_down  
    
    def shoot(self):
        
        
       
        bullet = Bullet()
        # Set the bullet so it is where the player is
        bullet.rect.x = self.rect.x
        bullet.rect.y = self.rect.y
        # Add the bullet to the lists
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)
                
        
class Enemy(pygame.sprite.Sprite):
    """ This class represents the enemy . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([25,25])
        self.image.fill(RED)
        
        self.rect = self.image.get_rect()
              
        
    def update(self):
        global player
        if self.rect.x != player.rect.x or self.rect.y != player.rect.y:
            # find normalized direction vector (dx, dy) between enemy and player
            dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
            dist = math.hypot(dx, dy)
            dx, dy = dx / dist, dy / dist
            # move along this normalized vector towards the player at current speed
            self.rect.x -= dx * 2
            self.rect.y -= dy * 2     
        
              
        
        
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self, x, y, angle, speed):
        pygame.sprite.Sprite.__init__(self)
        # Rotate the bullet image (negative angle because y-axis is flipped).
        self.image = pygame.transform.rotate(pygame.Surface([5,5]), angle)
        self.rect = self.image.get_rect(center=(x, y))
        angle = math.radians(angle)
        print(angle)
        self.speed_x = speed * math.cos(angle)
        self.speed_y = speed * math.sin(angle)       
               
        
        
        
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
            
        
        
def main():
    global player
    """ Main Program """
    pygame.init()
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
 
    pygame.display.set_caption("Topdown")
    
    # Create the player
    player = Player()   
    
    
    

    player.rect.x = 340
    player.rect.y = 300
    all_sprites_list.add(player)   
    

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()


    # -------- Main Program Loop -----------
    while not done:
        
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                # MOVEMENT #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_w:
                    player.go_up()
                if event.key == pygame.K_s:
                    player.go_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.new_x < 0:
                    player.new_x = 0
                if event.key == pygame.K_d and player.new_x > 0:
                    player.new_x = 0
                if event.key == pygame.K_w and player.new_y < 0:
                    player.new_y = 0
                if event.key == pygame.K_s and player.new_y > 0:
                    player.new_y = 0
                    
                    
                    # FIRING #
        key=pygame.key.get_pressed()  #checking pressed keys
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
                    
        
                   
                
                                 
                        	
                   
        
            
        if len(enemy_list) < 10:
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
                #score += 1
                #print(score)
    
            # Remove the bullet if it flies up off the screen
            if bullet.rect.y < -10 or bullet.rect.y > SCREEN_HEIGHT or bullet.rect.x > SCREEN_WIDTH or bullet.rect.x < -10:
                bullet_list.remove(bullet)
                all_sprites_list.remove(bullet)        
        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        screen.fill(WHITE)
        
        all_sprites_list.draw(screen)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()    
    
    
    
if __name__ == "__main__":
    main()
