import pygame
import random

# Initialize Pygame
pygame.init()

# LED Matrix Settings
GRID_SIZE = 8   # 8x8 LED grid

# Get screen dimensions dynamically
infoObject = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h

# Calculate LED size dynamically to fit the screen
LED_SIZE = min(WIDTH, HEIGHT) // GRID_SIZE

# Calculate the offset to center the grid on screen
OFFSET_X = (WIDTH - (GRID_SIZE * LED_SIZE)) // 2
OFFSET_Y = (HEIGHT - (GRID_SIZE * LED_SIZE)) // 2

SPEED_INCREMENT = 20
speed = 100

# Create screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("LED Racer")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Pause flag
paused = False

# Start the black square in the center
player_xy = [GRID_SIZE // 2, GRID_SIZE // 2]  # Use a list to allow modification

player_locations = set()

def player_tracker(player_xy):
    player_locations.add(tuple(player_xy))
    if len(player_locations) == GRID_SIZE * GRID_SIZE:
        player_locations.clear()

def draw_led_grid():
    """Draw the LED grid, with one black square at player_xy"""
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            # Adjust positions based on the offsets
            pos_x = OFFSET_X + x * LED_SIZE
            pos_y = OFFSET_Y + y * LED_SIZE
            
            if (x, y) == tuple(player_xy):  # Convert list to tuple for comparison
                pygame.draw.rect(screen, BLACK, (pos_x, pos_y, LED_SIZE, LED_SIZE))  # Dark square
                pygame.draw.rect(screen, WHITE, (pos_x, pos_y, LED_SIZE, LED_SIZE), 5)  
            elif (x, y) in player_locations:  # past locations
                pygame.draw.rect(screen, BLACK, (pos_x, pos_y, LED_SIZE, LED_SIZE))  # Dark square
                pygame.draw.rect(screen, BLACK, (pos_x, pos_y, LED_SIZE, LED_SIZE), 2)  
            else:
                color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))  # Brighter colors
                pygame.draw.rect(screen, color, (pos_x, pos_y, LED_SIZE, LED_SIZE))
                pygame.draw.rect(screen, BLACK, (pos_x, pos_y, LED_SIZE, LED_SIZE), 2)  
            
            # Draw grid outline
            pygame.draw.rect(screen, BLACK, (pos_x, pos_y, LED_SIZE, LED_SIZE), 2)

# Main loop
running = True
while running:
    screen.fill(BLACK)
    
    if not paused:  # Only update LEDs if not paused
        draw_led_grid()
        player_tracker(player_xy)
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
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:  # Quit on 'Q' or 'ESC' key press
                running = False
            if event.key == pygame.K_UP:
                if player_xy[1] > 0:  # Prevent moving out of bounds
                    player_xy[1] -= 1
            elif event.key == pygame.K_DOWN:
                if player_xy[1] < GRID_SIZE - 1:
                    player_xy[1] += 1
            elif event.key == pygame.K_LEFT:
                if player_xy[0] > 0:
                    player_xy[0] -= 1
            elif event.key == pygame.K_RIGHT:
                if player_xy[0] < GRID_SIZE - 1:
                    player_xy[0] += 1
            elif event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Speed up
                speed = max(20, speed - SPEED_INCREMENT)
            elif event.key == pygame.K_MINUS:  # Slow down
                speed += SPEED_INCREMENT

    pygame.time.delay(speed)  # Delay for smooth animation

pygame.quit()
