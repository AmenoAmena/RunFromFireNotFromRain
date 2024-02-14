import pygame
from sys import exit
from random import randint # We are just importing randint because we are just using randint and we are going to use a lot


pygame.init() # Starting the pygame library

score_started = False 

game_running = True

def keyboard():
    key = pygame.key.get_pressed() # Getting keyboard inputs
    if key[pygame.K_RIGHT] or key[pygame.K_d]: # If a or left pressed
        player.x += player_speed # We are changing x corrdinate of our player with using right key or d


    if key[pygame.K_LEFT] or key[pygame.K_a]: # If a or left pressed
        player.x -= player_speed # We are changing x corrdinate of our player with using left key or a

    # With these statements if players x is > 1140 or < 0 we are resetting its position
    # With this statement player can't get out of screen
    if player.x >= 1140: # We are limiting players x position
        player.x = 1140
    
    if player.x <= 0: # We are limiting players x position
        player.x = 0


game_active = False # For game states

screen_fill_blue = (51,255,255)# Color that changes through score number

game_number = 0 # For writing the number of games to score.txt
game_number_valid = True # For not write more than 1 each time

width = 1200 # Width of the gamescreen
height = 600 # Height of the game screen
# First argument->width,second argument -> height
screen = pygame.display.set_mode((width, height)) # Creating the screen 

fps = 60 # Our fps number
clock = pygame.time.Clock() # Adjusting the frames per second for game

when_filled = (0,0,0) # For the lives and score after background color changes

# Speeds
player_speed = 8 # Our players speed

player_color = (0,102,51)

# For start the game
font = pygame.font.SysFont('consolas',24) # Our basic font 
# font_names = pygame.font.get_fonts() -> print this to see all fonts
text_start = font.render("Press space to start the game",True,(0,0,0)) # Creating a press space to start game text
text_start_coordinate = text_start.get_rect() # Creating a coordinate (empty) for text_start
text_start_coordinate.center = (600,300) # Adjusting the coordiante (non-empty) for text_start


# For congrats
text_congrats = font.render("Congrats max score",True,(0,0,0)) # Creates a congrats text
text_congrats_coordinate = text_congrats.get_rect() # Creating a coordinate (empty) for text_congrats
text_congrats_coordinate.center = (600,200) # Adjusting the coordiante (non-empty) for text_congrats


# Exit test
text_exit = font.render("Press q to exit",True,(0,0,0)) # Creates an exit text
text_exit_coordinate = text_exit.get_rect() # Creating a coordinate (empty) for text_exit
text_exit_coordinate.center = (600,400) # Adjusting the coordinate (non-empty) for text_exit

# Score System
score = 0 # Creating a score counter
text_score = font.render("Score:" + str(score),True,(0,0,0)) # For creating a score text
text_score_active = font.render("Score:" + str(score),True,(when_filled)) # For creating a score system inside the game
text_score_coordinate = text_score.get_rect() # Creating a coordinate (empty) for text_score
text_score_active_coordinate = text_score.get_rect() # Creating a coordinate (empty) for text_score_active
text_score_active_coordinate.center = (80,50) # Adjusting coordinate (non-empty) for text_score
text_score_coordinate.center = (600,350) # Adjusting coordinate (non-empty) for text_score



# Live System
live = 3 # Adjust how many lives does player has
text_live = font.render("Lives:" + str(live),True,(when_filled)) # For cerating live text
text_live_coordinate = text_live.get_rect() # Creating a coordinate (empty) for text_live
text_live_coordinate.center = (1140,20) # Adjusting coordinate (non-empty) for text_live

blacked = False # Creates fro making background black

# Score written
score_written = True # For writing score once

# Sun
sun = pygame.Rect(1050,50,60,60) # Creating sun element

# Ground
ground = pygame.Rect(0,400,1200,200) # Creating ground element

# Player
player = pygame.Rect(200,340,60,60) # Creating player element

# Fires
fire1_rand = randint(0,240) # Make fire 1's x random and make it can be changed
fire2_rand = randint(240,480) # Make fire 2's x random and make it can be changed
fire3_rand = randint(480,720) # Make fire 3's x random and make it can be changed
fire4_rand = randint(720,960) # Make fire 4's x random and make it can be changed
fire5_rand = randint(960,1200) # Make fire 5's x random and make it can be changed

fire1_speed = randint(6,10) # Make the speed randomize for fire 1
fire2_speed = randint(6,10) # Make the speed randomize for fire 1
fire3_speed = randint(6,10) # Make the speed randomize for fire 1
fire4_speed = randint(6,10) # Make the speed randomize for fire 1
fire5_speed = randint(6,10) # Make the speed randomize for fire 1

#For increasing live
live_checked_10 = False # Creates a boolean for when score = 10 inrease live by 1 
live_checked_20 = False # Creates a boolean for when score = 10 inrease live by 2
live_checked_30 = False # Creates a boolean for when score = 10 inrease live by 3
live_checked_40 = False # Creates a boolean for when score = 10 inrease live by 4
# Not made for 50 because when score = 50 game will end

fire1 = pygame.Rect(fire1_rand,-10,80,80) # Creating first fire element
fire2 = pygame.Rect(fire2_rand,-10,80,80) # Creating second fire element
fire3 = pygame.Rect(fire3_rand,-10,80,80) # Creating third fire element
fire4 = pygame.Rect(fire4_rand,-10,80,80) # Creating fourth fire element
fire5 = pygame.Rect(fire5_rand,-10,80,80) # Creating fifth fire element

#Rain
rain1_speed = randint(8,12) # Make first rains speed randomized
rain1 = pygame.Rect(randint(0,1200),-100,80,80) # Creating first rain element

rain2_speed = randint(8,12) # Make second rains speed randomized
rain2 = pygame.Rect(randint(0,1200),-100,80,80) # Creating second rain element

black = (0,0,0) # Make a black color

# (red,green,blue) -> (255,255,255)White

while True: #Making game loop
    for event in pygame.event.get(): # Opening event loop
        if event.type == pygame.QUIT: # Making a thing when pressed exit
            with open("score.txt","a") as file: # Opening score.txt file in append mode
                file.write("------------------\n") # Writes ------------------ and get to the under line 
            pygame.quit() # Closes pygame library
            exit() # Exits the program
        
        if event.type == pygame.KEYDOWN: # Creating a thing when pressed for keyboard
            if event.key == pygame.K_SPACE and game_active == False and game_number_valid == True: # When space pressed do things
                game_active = True # Makeing game active true for changing game state
                score = 0 # With making game state active reset the score
                game_number += 1 # Make game number incresed by 1 for when writing files know which game is it
            else: 
                pass # Dont do anything
            if event.key == pygame.K_q: # If q pressed do these
                with open("score.txt","a") as file: # Opening score.txt in append mode
                    file.write("------------------\n") # Writes ------------------ and get to the under line
                pygame.quit() # Closes pygame library
                exit() # Exits the program
            
            if event.key == pygame.K_b: # If b pressed do these
                blacked = True # Make blacked true for making background color black
            if event.key == pygame.K_w: # If w pressed do these
                blacked = False # Make blacked false for getting back randomized background colors


    if game_active: # When game state is game_active
        keyboard() # Using keyboard function
        

        #Fire System
        fire1.y += fire1_speed # Make fire1's y coordinate get down by fire1_speed
        if fire1.y > 360: # When fire1's y coordiante bigger than 360 do these
            fire1.y = randint(-400,-100) # Resets fire1's y coordinate between -400 and -100
            fire1.x = randint(0,240) # Resets fire1's x coordinate between 0 and 240
            fire1_speed = randint(6,10) # Re randomize fire1's speed
            fire1.y += fire1_speed # Make fire1's y coordinate get down by fire1_speed
        
        fire2.y += fire2_speed # Make fire2's y coordinate get down by fire2_speed
        if fire2.y > 360: # When fire2's y coordiante bigger than 360 do these
            fire2.y = randint(-400,-100) # Resets fire2's y coordinate between -400 and -100
            fire2.x = randint(240,480) # Resets fire2's x coordinate between 240 and 480
            fire2_speed = randint(6,10) # Make fire2's y coordinate get down by fire2_speed

        fire3.y += fire3_speed # Make fire3's y coordinate get down by fire3_speed
        if fire3.y > 360: # When fire3's y coordiante bigger than 360 do these
            fire3.y = randint(-400,-100) # Resets fire3's y coordinate between -400 and -100
            fire3.x = randint(480,720) # Resets fire3's x coordinate between 480 and 720
            fire3_speed = randint(6,10) # Make fire3's y coordinate get down by fire3_speed


        fire4.y += fire4_speed # Make fire4's y coordinate get down by fire4_speed
        if fire4.y > 360: # When fire4's y coordiante bigger than 360 do these
            fire4.y = randint(-400,-100) # Resets fire4's y coordinate between -400 and -100
            fire4.x = randint(720,960) # Resets fire4's x coordinate between 720 and 960
            fire4_speed = randint(6,10) # Make fire4's y coordinate get down by fire4_speed


        fire5.y += fire5_speed # Make fire5's y coordinate get down by fire5_speed
        if fire5.y > 360: # When fire5's y coordiante bigger than 360 do these
            fire5.y = randint(-400,-100) # Resets fire5's y coordinate between -400 and -100
            fire5.x = randint(960,1200) # Resets fire5's x coordinate between 960 and 1200
            fire5_speed = randint(6,10)  # Make fire5's y coordinate get down by fire5_speed

        
        if fire1.colliderect(player): # If player rectangle collides with fire1 rectangle do these
            live -= 1 # Decrese live by one
            fire1.y = randint(-400,-100) # Sets fire1's y coordinate between -400 and -100
            fire1.x = randint(0,240) # Set fire1's x coordinate between 0 and 240
            fire1_speed = randint(6,10) # Make fire1's speed between 6 and 10
            fire1.y += fire1_speed # Decreasing fire1's y coordinate decreasing by randomized fire1_speed
        
        
        if fire2.colliderect(player): # If player rectangle collides with fire2 rectangle do these
            live -= 1 # Decrese live by one
            fire2.y = randint(-400,-100) # Sets fire2's y coordinate between -400 and -100
            fire2.x = randint(0,240) # Set fire2's x coordinate between 240 and 480
            fire2_speed = randint(6,10) # Make fire2's speed between 6 and 10
            fire2.y += fire2_speed # Decreasing fire2's y coordinate decreasing by randomized fire2_speed

        if fire3.colliderect(player): # If player rectangle collides with fire3 rectangle do these
            live -= 1 # Decrese live by one
            fire3.y = randint(-400,-100) # Sets fire3's y coordinate between -400 and -100
            fire3.x = randint(0,240) # Set fire3's x coordinate between 480 and 720
            fire3_speed = randint(6,10) # Make fire3's speed between 6 and 10
            fire3.y += fire3_speed # Decreasing fire3's y coordinate decreasing by randomized fire3_speed

        if fire4.colliderect(player): # If player rectangle collides with fire4 rectangle do these
            live -= 1 # Decrese live by one
            fire4.y = randint(-400,-100) # Sets fire4's y coordinate between -400 and -100
            fire4.x = randint(0,240) # Set fire1's x coordinate between 720 and 960
            fire4_speed = randint(6,10) # Make fire4's speed between 6 and 10
            fire4.y += fire4_speed # Decreasing fire4's y coordinate decreasing by randomized fire4_speed

        if fire5.colliderect(player): # If player rectangle collides with fire5 rectangle do these
            live -= 1 # Decrese live by one
            fire5.y = randint(-400,-100) # Sets fire5's y coordinate between -400 and -100 
            fire5.x = randint(960,1200) # Set fire1's x coordinate between 960 and 1200
            fire5_speed = randint(6,10) # Make fire5's speed between 6 and 10
            fire5.y += fire5_speed # Decreasing fire5's y coordinate decreasing by randomized fire5_speed

    # Rain System
    rain1.y += rain1_speed # Make rain1's y coordinate get down by rain1_speed
    if rain1.colliderect(player): # If player rectangle collides with rain1 rectangle do these
        rain1.y = randint(-800,-0) # Sets rain1's y coordinate between -800 and 0
        rain1.x = randint(0,1200) # Set rain1's x coordinate between 0 and 1200
        rain1_speed = randint(8,12) # Makes rain1's speed between 8 and 12
        score += 1 # Increase sports by one
        screen_fill_blue = (randint(0,255),randint(0,255),randint(0,255)) # Changing screen_fill_blue for changing the background

    
    
    if rain1.y > 600: # If rain1's y coordinate bgger than 600
        rain1.y = randint(-800,-0) # Sets rain1's y coordinate between -800 and 0
        rain1.x = randint(0,1200) # Set rain1's x coordinate between 0 and 1200
        rain1_speed = randint(8,12) # Makes rain1's speed between 8 and 12


 

    rain2.y += rain2_speed # Make rain2's y coordinate get down by rain2_speed
    if rain2.colliderect(player): # If player rectangle collides with rain2 rectangle do these
        rain2.y = randint(-800,-0) # Sets rain2's y coordinate between -800 and 0
        rain2.x = randint(0,1200) # Set rain2's x coordinate between 0 and 1200
        rain2_speed = randint(8,12) # Makes rain2's speed between 8 and 12
        score += 1 # Increase sports by one
        screen_fill_blue = (randint(0,255),randint(0,255),randint(0,255)) # Changing screen_fill_blue for changing the background



    if rain2.y > 600:
        rain2.y = randint(-800,-0)
        rain2.x = randint(0,1200)
        rain2_speed = randint(8,12)


    #color change system
    if score == 10:
        if live_checked_10 == False:
            live += 1
            live_checked_10 = True
            player_color = (randint(0,255),0,randint(0,255))
        else:
            pass


    if score == 20:
        if live_checked_20 == False:
            live += 1
            live_checked_20 = True
            player_color = (randint(0,255),0,randint(0,255))
        else:
            pass

    if score == 30:
        when_filled = (255,255,255)
        if live_checked_30 == False:
            live += 1
            live_checked_30 = True
            player_color = (randint(0,255),0,randint(0,255))
        else:
            pass

    if score == 40:
        if live_checked_40 == False:
            live += 1
            live_checked_40 = True
            player_color = (randint(0,255),0,randint(0,255))
        else:
            pass 
    if score >= 50:
        game_active = False

    text_score = font.render("Score:" + str(score),True,(when_filled))
    text_score_active = font.render("Score:" + str(score),True,(when_filled))
    text_live = font.render("Lives:" + str(live),True,(when_filled))

    if blacked:
        when_filled = (255,255,255)
    if not blacked:
        when_filled = (0,0,0)

    if live == 0:
        game_active = False


    if game_active:
        score_started = True
        score_written = True
        game_number_valid = False
        if blacked:       
            screen.fill(black)
        else:
            screen.fill(screen_fill_blue)
        pygame.draw.ellipse(screen,(255,255,0),sun)
        pygame.draw.rect(screen,(153,76,0),ground)
        pygame.draw.rect(screen,(player_color),player)
        pygame.draw.ellipse(screen,(153,0,0),fire1)
        pygame.draw.ellipse(screen,(153,0,0),fire2)
        pygame.draw.ellipse(screen,(153,0,0),fire3)
        pygame.draw.ellipse(screen,(153,0,0),fire4)
        pygame.draw.ellipse(screen,(153,0,0),fire5)
        pygame.draw.ellipse(screen,(0,0,153),rain1)
        pygame.draw.ellipse(screen,(0,0,153),rain2)
        screen.blit(text_score_active,text_score_active_coordinate)
        screen.blit(text_live,text_live_coordinate)
    
    if not game_active:
        live_checked_10 = False
        live_checked_20 = False
        live_checked_30 = False
        live_checked_40 = False

        when_filled = (0,0,0)
        screen_fill_blue = (51,255,255)
        game_number_valid = True
        screen.fill((255,255,255))
        if score >= 50:
            screen.blit(text_congrats,text_congrats_coordinate)
        else:
            pass
        screen.blit(text_start,text_start_coordinate)
        screen.blit(text_score,text_score_coordinate)
        screen.blit(text_exit,text_exit_coordinate)
        
        live = 3
        
        fire1.x = fire1_rand
        fire2.x = fire2_rand
        fire3.x = fire3_rand
        fire4.x = fire4_rand
        fire5.x = fire5_rand

        fire1.y = randint(-300,-100)
        fire2.y = randint(-300,-100)
        fire3.y = randint(-300,-100)
        fire4.y = randint(-300,-100)
        fire5.y = randint(-300,-100)

        rain1.x = randint(0,1200)
        rain2.x = randint(0,1200)

        rain1.y = randint(-800, 0)
        rain2.y = randint(-800,0)

        player.x = 540 
        player.y = 340

        if score_written and score_started:
            with open("score.txt","a") as file:
                file.write(f"{game_number}. Score: {score}\n") 
            score_written = False



    pygame.display.update()
    clock.tick(fps)



