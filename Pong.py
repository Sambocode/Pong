# Example file showing a circle moving on screen
import pygame
import random

pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('Comic Sans MS', 30)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 600))

display_width = 800
display_height = 600



#pygame.mixer.init()

#pygame.mixer.music.load('gaming.mp3')
#pygame.mixer.music.play()
#player_pos = pygame.Vector2(screen.get_width() / 2 -16, screen.get_height() / 2 -16)
#enemy_pos = pygame.Vector2(100,100)
#gameDisplay = pygame.display.set_mode((display_width,display_height))




def game():
 
    p1Pos = pygame.Vector2(10,10)
    p2Pos = pygame.Vector2(screen.get_width() - 20,screen.get_height() -70)
    bPos = pygame.Vector2(screen.get_width()/2 - 5,screen.get_height()/2 -5)
    bSpeedy = 100
    bSpeedx = 100
    vel = 1
    dt = 0
    p1Score = 0
    p2Score = 0
    p1ScorePrint = str(p1Score)
    p2ScorePrint = str(p2Score)
    text_surface = my_font.render(p1ScorePrint, False, (0, 0, 250))
    text_surface2 = my_font.render(p2ScorePrint, False, (0, 0, 250))
    clock = pygame.time.Clock()

    while True:


        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")
        currentTime = pygame.time.get_ticks()
        print(currentTime/1000)
        seconds = currentTime/1000

        randNum = random.randrange(5,10,1)

        if(seconds > (10+randNum)):
            vel = 2

        if(seconds > (20+randNum)):
            vel = 3
        
        #score
        p1ScorePrint = str(p1Score)
        p2ScorePrint = str(p2Score) 
        text_surface = my_font.render(p1ScorePrint, False, (255, 255, 255))
        text_surface2 = my_font.render(p2ScorePrint, False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width()/2 -70,0))
        screen.blit(text_surface2, (screen.get_width()/2 +50,0))


        #pygame.draw.circle(screen, "white", player_pos, 20)
    # ship = pygame.image.load('ship.png')
        #enemy = pygame.draw.circle(screen,"red",enemy_pos,10)
    # gameDisplay.blit(ship, (player_pos))
        
        p1 = pygame.draw.rect(screen,"white",(p1Pos.x,p1Pos.y,10,50))
        p2 = pygame.draw.rect(screen,"white",(p2Pos.x,p2Pos.y,10,50))
        ball = pygame.draw.rect(screen,"white",(bPos.x,bPos.y,10,10))
        #ball movement
        bPos.x += bSpeedx * vel * dt
        bPos.y += bSpeedy * vel * dt
        
        if(bPos.y >= 600 -10 or bPos.y <= 0):
            bSpeedy = -bSpeedy
    # if(bPos.x >= 800 -10 or bPos.x <=0):
        #  bSpeedx = -bSpeedx
        if(bPos.x < p1Pos.x +10 and bPos.y > p1Pos.y and bPos.y < p1Pos.y +50):
            bSpeedx = -bSpeedx 

        if(bPos.x + 10  > p2Pos.x  and bPos.y > p2Pos.y and bPos.y < p2Pos.y +50):
            bSpeedx = -bSpeedx 

        #movement p1s
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            p1Pos.y -= 300 * vel * dt
        if keys[pygame.K_s]:
            p1Pos.y += 300 * vel* dt
            """
        if keys[pygame.K_a]:
            p1Pos.x -= 300 * dt
        if keys[pygame.K_d]:
            p1Pos.x += 300 * dt
            """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            p2Pos.y -= 300 * vel * dt
        if keys[pygame.K_DOWN]:
            p2Pos.y += 300 * vel * dt
            """
        if keys[pygame.K_LEFT]:
            p2Pos.x -= 300 * dt
        if keys[pygame.K_RIGHT]:
            p2Pos.x += 300 * dt
        """
        #limits
        if(p1Pos.y <= 0):
            p1Pos.y = 0
        if(p1Pos.y + 50 >= 600):
            p1Pos.y = 550

        if(p2Pos.y <= 0):
            p2Pos.y = 0
        if(p2Pos.y + 50 >= 600):
            p2Pos.y = 550


        #score
        if(ball.x < 0 ):
            p2Score += 1
            bPos = pygame.Vector2(screen.get_width()/2 - 5,screen.get_height()/2 -5)
            print(p2Score)
            continue

        if(ball.x > 800 ):
            p1Score += 1
            bPos = pygame.Vector2(screen.get_width()/2 - 5,screen.get_height()/2 -5)
            print(p1Score)
            continue

        if(p1Score == 5):
            print("player 1 wins")
            global winner
            winner = "Player 1"
            end()

        if(p2Score == 5):
            print("player 2 wins")
            winner = "Player 2"
            end()
            
        


        #collision
    # if(player_pos.x <= 100):
        #    print("hello im workings")
        
        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000


def menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill('navy')
        text_surface = my_font.render("Player 1 W and S, Player 2 Up and Down", False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width()/2 -250,200))
        text_surface = my_font.render("Press space to battle", False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width()/2 -150,300))
        text_surface = my_font.render("First to 5", False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width()/2 -75,500))
        pygame.display.flip()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            break
        
def end():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill('darkviolet')
        text_surface = my_font.render(winner + " Wins", False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width()/2 -150,200))
        text_surface = my_font.render("Space key to battle more", False, (255, 255, 255))
        screen.blit(text_surface, (screen.get_width()/2 -150,300))
        pygame.display.flip()
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game()

menu()
game()
end()

