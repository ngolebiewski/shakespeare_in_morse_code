import pygame
import random

# Initialize Pygame
pygame.init()

# LED Matrix Settings
LED_SIZE = 40  # Each LED is a 40x40 pixel square
GRID_SIZE = 8   # 8x8 LED grid
WIDTH, HEIGHT = GRID_SIZE * LED_SIZE, GRID_SIZE * LED_SIZE
SPEED_INCREMENT = 20
speed = 100

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LED Pixel Display Simulation")

# Colors
BLACK = (0, 0, 0)

# Pause flag
paused = False

# Start the black square in the center
location_coordinate = [GRID_SIZE // 2, GRID_SIZE // 2]  # Use a list to allow modification

def draw_led_grid():
    """Draw the LED grid, with one black square at location_coordinate"""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if (x, y) == tuple(location_coordinate):  # Convert list to tuple for comparison
                pygame.draw.rect(screen, BLACK, (x * LED_SIZE, y * LED_SIZE, LED_SIZE, LED_SIZE))  # Dark square
            else:
                color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))  # Brighter colors
                pygame.draw.rect(screen, color, (x * LED_SIZE, y * LED_SIZE, LED_SIZE, LED_SIZE))
            
            # Draw grid outline
            pygame.draw.rect(screen, BLACK, (x * LED_SIZE, y * LED_SIZE, LED_SIZE, LED_SIZE), 2)  

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    if not paused:  # Only update LEDs if not paused
        draw_led_grid()
        pygame.display.flip()
    
    # draw_led_grid()  # Always redraw the grid so movement updates
    # pygame.display.flip()
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            paused = True  # Pause animation on mouse hold
        elif event.type == pygame.MOUSEBUTTONUP:
            paused = False  # Resume animation on mouse release
        elif event.type == pygame.KEYDOWN:  # Detect key presses
            if event.key == pygame.K_UP:
                if location_coordinate[1] > 0:  # Prevent moving out of bounds
                    location_coordinate[1] -= 1
            elif event.key == pygame.K_DOWN:
                if location_coordinate[1] < GRID_SIZE - 1:
                    location_coordinate[1] += 1
            elif event.key == pygame.K_LEFT:
                if location_coordinate[0] > 0:
                    location_coordinate[0] -= 1
            elif event.key == pygame.K_RIGHT:
                if location_coordinate[0] < GRID_SIZE - 1:
                    location_coordinate[0] += 1
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Speed up
                speed = max(20, speed - SPEED_INCREMENT)
            elif event.key == pygame.K_MINUS:  # Slow down
                speed += SPEED_INCREMENT

    pygame.time.delay(speed)  # Delay for smooth animation

pygame.quit()
