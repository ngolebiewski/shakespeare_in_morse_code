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


# Create a random LED pattern
def draw_led_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Random color
            pygame.draw.rect(screen, color, (x * LED_SIZE, y * LED_SIZE, LED_SIZE, LED_SIZE))
            pygame.draw.rect(screen, BLACK, (x * LED_SIZE, y * LED_SIZE, LED_SIZE, LED_SIZE), 2)  # Grid outline

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    if not paused:  # Only update LEDs if not paused
        draw_led_grid()
        pygame.display.flip()
    
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
                if speed > 0: 
                    speed -= SPEED_INCREMENT # Make speed of pixels faster
                print(speed)
            elif event.key == pygame.K_DOWN:
                speed += SPEED_INCREMENT # Make speed of pixels slower
                print(speed)
            

    pygame.time.delay(speed)  # Delay for smooth animation

pygame.quit()
