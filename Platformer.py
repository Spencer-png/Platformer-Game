import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player properties
player_width = 40
player_height = 60
player_x = 50
player_y = HEIGHT - player_height
player_speed = 5
player_jump = 15
player_gravity = 0.8
player_velocity = 0

# Platform properties
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
    pygame.Rect(300, 400, 200, 20),
    pygame.Rect(100, 300, 200, 20),
    pygame.Rect(500, 200, 200, 20),
]

# Game loop
clock = pygame.time.Clock()
running = True
can_jump = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and can_jump:
                player_velocity = -player_jump
                can_jump = False

    keys = pygame.key.get_pressed()
    
    # Move left/right
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Apply gravity
    player_velocity += player_gravity
    player_y += player_velocity

    # Check for collisions with platforms
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    for platform in platforms:
        if player_rect.colliderect(platform):
            if player_velocity > 0:
                player_y = platform.top - player_height
                player_velocity = 0
                can_jump = True
            elif player_velocity < 0:
                player_y = platform.bottom
                player_velocity = 0

    # Keep player on screen
    player_x = max(0, min(player_x, WIDTH - player_width))
    
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, platform)
    
    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_width, player_height))
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()