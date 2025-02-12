import asyncio
import pygame
import random
import sys

async def main():
    # Initialize Pygame with explicit display driver
    pygame.init()
    
    # Constants
    GRID_SIZE = 8
    WIDTH = 480
    HEIGHT = 480
    
    # Print debug info
    print("Initializing game...")
    print(f"Pygame version: {pygame.version.ver}")
    print(f"Display drivers: {pygame.display.get_driver()}")
    
    # Setup display with explicit software rendering
    screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.SCALED)
    pygame.display.set_caption("LED Eraser Racer")
    
    print("Display initialized...")
    
    LED_SIZE = min(WIDTH, HEIGHT) // GRID_SIZE
    OFFSET_X = (WIDTH - (GRID_SIZE * LED_SIZE)) // 2
    OFFSET_Y = (HEIGHT - (GRID_SIZE * LED_SIZE)) // 2
    
    # Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    
    # Game state
    speed = 100
    paused = False
    player_xy = [GRID_SIZE // 2, GRID_SIZE // 2]
    player_locations = set()
    
    print("Game variables initialized...")
    
    def player_tracker(player_xy):
        player_locations.add(tuple(player_xy))
        if len(player_locations) > GRID_SIZE * GRID_SIZE * 2:
            player_locations.clear()
    
    def draw_led_grid():
        try:
            screen.fill(BLACK)  # Clear screen first
            for y in range(GRID_SIZE):
                for x in range(GRID_SIZE):
                    pos_x = OFFSET_X + x * LED_SIZE
                    pos_y = OFFSET_Y + y * LED_SIZE
                    rect = pygame.Rect(pos_x, pos_y, LED_SIZE, LED_SIZE)
                    
                    if (x, y) == tuple(player_xy):
                        pygame.draw.rect(screen, BLACK, rect)
                        pygame.draw.rect(screen, WHITE, rect, 3)
                    elif (x, y) in player_locations:
                        pygame.draw.rect(screen, BLACK, rect)
                        pygame.draw.rect(screen, BLACK, rect, 2)
                    else:
                        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
                        pygame.draw.rect(screen, color, rect)
                        pygame.draw.rect(screen, BLACK, rect, 2)
        except Exception as e:
            print(f"Drawing error: {e}")
    
    print("Starting game loop...")
    
    # Main game loop
    running = True
    while running:
        try:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_UP and player_xy[1] > 0:
                        player_xy[1] -= 1
                    elif event.key == pygame.K_DOWN and player_xy[1] < GRID_SIZE - 1:
                        player_xy[1] += 1
                    elif event.key == pygame.K_LEFT and player_xy[0] > 0:
                        player_xy[0] -= 1
                    elif event.key == pygame.K_RIGHT and player_xy[0] < GRID_SIZE - 1:
                        player_xy[0] += 1
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    paused = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    paused = False
            
            if not paused:
                draw_led_grid()
                player_tracker(player_xy)
                pygame.display.flip()
            
            # Web-specific: ensure proper frame timing
            await asyncio.sleep(0)
            if not paused:
                await asyncio.sleep(speed / 1000)
                
        except Exception as e:
            print(f"Game loop error: {e}")
            break
    
    print("Game closing...")
    pygame.quit()

if __name__ == "__main__":
    asyncio.run(main())