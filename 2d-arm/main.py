import pygame
import sys

# classes
from classes.Arm import Arm

def main():
    pygame.init()

    # Set the dimensions of the window
    window_size = (800, 600)
    window_midpoints = [window_size[i]/2 for i in range(len(window_size))]
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("2D Arm")
    
    background_color = (255, 255, 255)
    
    arm = Arm((400, 300), 100, 3)    
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # also check to see if mouse is over object
                print("mouse down")
            elif event.type == pygame.MOUSEBUTTONUP:
                # check to see if already draggin
                print("mouse up")
                
        screen.fill(background_color)
                
        mouse_pos = pygame.mouse.get_pos()
        arm.update_end_effector_pos(mouse_pos)        
        
        arm.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
