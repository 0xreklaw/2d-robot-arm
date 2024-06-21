import pygame
import sys

# Classes and objects import
from classes.Arm import Arm
from classes.Fruit import Fruit
from objects import apple, table, orange, grape, strawberry, watermelon_slice, pineapple, pear

def main():
    pygame.init()

    # Set the dimensions of the window
    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("2D Arm")
    
    background_color = (255, 255, 255)
    table_height = 500
    
    arm = Arm((400, table_height), 100, 3)

    fruits = [
        Fruit(apple, 120, table_height - 25),
        # Fruit(orange, 150, table_height - 50),
        Fruit(grape, 200, table_height - 50),
        Fruit(strawberry, 250, table_height - 50),
        # Fruit(watermelon_slice, 300, table_height - 50),
        # Fruit(pineapple, 350, table_height - 50),
        # Fruit(pear, 400, table_height - 50),
    ]

    
    selected_fruit = None
    
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for fruit in fruits:
                    if fruit.is_mouse_over(pygame.mouse.get_pos()):
                        fruit.dragging = True
                        selected_fruit = fruit
                        break
            elif event.type == pygame.MOUSEBUTTONUP:
                if selected_fruit:
                    selected_fruit.dragging = False
                    selected_fruit = None
        
        if selected_fruit:
            selected_fruit.x, selected_fruit.y = pygame.mouse.get_pos()
        
        screen.fill(background_color)
        
        # Draw left table with fruits
        table(screen, 200, table_height)
        
        # Draw right table (empty initially)
        table(screen, 600, table_height)
        
        for fruit in fruits:
            fruit.draw(screen)
                
        mouse_pos = pygame.mouse.get_pos()
        arm.update_end_effector_pos(mouse_pos)
        
        arm.draw(screen)
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
