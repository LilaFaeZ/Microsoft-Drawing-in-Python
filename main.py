import pygame
from pygame.locals import *
# PSEUDOCODE FOR GAME:
# Track cursor
# On mouse1 hold: change cursor color

dic = {pygame.K_1 : pygame.Color(0,0,0), pygame.K_2 : pygame.Color(255,0,0), pygame.K_3 : pygame.Color(0,255,0), pygame.K_4 : pygame.Color(0,0,255), pygame.K_5 : pygame.Color(0,255,255)} #event.type = k_#
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True 
    is_painting = False
    dt = 0 #delta time, change in time
    screen.fill((255,255,255))
    x = (0,0,0) #permanent
    while(running): #while running is true
        mouse_pos = pygame.mouse.get_pos() #returns a tuple for the x,y of mouse

        for event in pygame.event.get(): #gets a list of every single event that is done 
            #in each frame
            if event.type == pygame.QUIT:
                running = False #checking if you closed the game
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_painting = not is_painting #changes value of is_painting (false) to (true)
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                print("key pressed")
                for i in range(pygame.K_1,pygame.K_5):
                    if keys[i] == True:
                        x = dic[i]
        if is_painting: #if true
            pygame.draw.rect(screen,x,(mouse_pos[0],mouse_pos[1],4,4), 0) #built in function
            #function above takes (surface, color of surface, rectangle to surface (what its draw,
            # left most, right most, 2 and 2 is width)
        pygame.display.flip()

            

        
    
main()