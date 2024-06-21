import pygame

# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (139, 69, 19)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)

# Function to draw an apple
def apple(surface, x, y):
    pygame.draw.circle(surface, RED, (x, y), 20)
    pygame.draw.rect(surface, BROWN, (x - 2, y - 30, 4, 10))

# Function to draw a table
def table(surface, x, y):
    pygame.draw.rect(surface, BROWN, (x - 100, y, 200, 20))  # Table top
    pygame.draw.rect(surface, BROWN, (x - 90, y + 20, 20, 80))  # Left leg
    pygame.draw.rect(surface, BROWN, (x + 70, y + 20, 20, 80)) 


# Function to draw an orange
def orange(surface, x, y):
    pygame.draw.circle(surface, ORANGE, (x, y), 20)

# Function to draw a grape
def grape(surface, x, y):
    for i in range(3):
        for j in range(3):
            pygame.draw.circle(surface, PURPLE, (x + i * 15, y + j * 15), 10)

# Function to draw a strawberry
def strawberry(surface, x, y):
    pygame.draw.ellipse(surface, RED, (x, y, 30, 40))
    pygame.draw.polygon(surface, GREEN, [(x + 15, y - 10), (x + 5, y), (x + 25, y)])


# Function to draw a watermelon slice
def watermelon_slice(surface, x, y):
    pygame.draw.polygon(surface, RED, [(x, y), (x + 50, y), (x + 25, y - 40)])
    pygame.draw.polygon(surface, GREEN, [(x, y), (x + 50, y), (x + 25, y - 10)])

# Function to draw a pineapple
def pineapple(surface, x, y):
    pygame.draw.ellipse(surface, YELLOW, (x, y, 30, 50))
    pygame.draw.polygon(surface, GREEN, [(x + 15, y - 20), (x + 5, y), (x + 25, y)])

# Function to draw a pear
def pear(surface, x, y):
    pygame.draw.ellipse(surface, GREEN, (x, y, 30, 40))
    pygame.draw.polygon(surface, BROWN, [(x + 15, y - 10), (x + 10, y), (x + 20, y)])
