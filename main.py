## TODO ##

# Topdown Shooter
# By NoiseGenerator
# Licensed under GNU GPL

import pygame, random
pygame.init()
all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

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
    
    def shoot(self, angle):
        bullet = Bullet()
        # Set the bullet so it is where the player is
        bullet.rect.x = self.rect.x
        bullet.rect.y = self.rect.y
        # Add the bullet to the lists
        all_sprites_list.add(bullet)
        bullet_list.add(bullet)
        bullet.angle = angle        
    
class Bullet(pygame.sprite.Sprite):
    """ This class represents the bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4, 4])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
        self.angle = 0
        
    def update(self):
        """ Move the bullet. """
        if self.angle == 0:
            self.rect.y -= 6
        if self.angle == 1:
            self.rect.x += 6
        if self.angle == 2:
            self.rect.y += 6
        if self.angle == 3:
            self.rect.x -= 6
        
def main():
    
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.shoot(3)
                    
                if event.key == pygame.K_RIGHT:
                    player.shoot(1)
                    
                if event.key == pygame.K_UP:
                    player.shoot(0)
                    
                if event.key == pygame.K_DOWN:
                    player.shoot(2)              
        
                        	
                    
            
                


        all_sprites_list.update() 
        # Calculate mechanics for each bullet
        for bullet in bullet_list:
    
            ## See if it hit a block
            #block_hit_list = pygame.sprite.spritecollide(bullet, block_list, True)
    
            ## For each block hit, remove the bullet and add to the score
            #for block in block_hit_list:
                #bullet_list.remove(bullet)
                #all_sprites_list.remove(bullet)
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
