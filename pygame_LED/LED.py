import pygame
import random
import time

# Initialize Pygame
pygame.init()

# LED Matrix Settings
LED_SIZE = 80  # Each LED is a 20x20 pixel square
GRID_SIZE = 8  # 8x8 LED grid
WIDTH, HEIGHT = GRID_SIZE * LED_SIZE, GRID_SIZE * LED_SIZE + 400

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LED Pixel Display Simulation")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a random LED pattern
def draw_led_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
            pygame.draw.rect(screen, color, (x * LED_SIZE, y * LED_SIZE, LED_SIZE, LED_SIZE))
            pygame.draw.rect(screen, BLACK, (x * LED_SIZE, y * LED_SIZE, LED_SIZE, LED_SIZE), 1)  # Grid outline

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    draw_led_grid()  # Draw the LEDs
    time.sleep(.1)
    
    pygame.display.flip()
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
