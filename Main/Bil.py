import pygame
import os
pygame.font.init()
pygame.mixer.init()

# Screen dimensions and setup
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game settings
FPS = 60
VEL = 5
car_WIDTH, car_HEIGHT = 55, 40

# Health settings
HEALTH_FONT = pygame.font.SysFont("helvetica", 30)
CAR_HIT = pygame.USEREVENT + 1  # Define custom event for car hit

# Load car image
car_IMAGE = pygame.image.load(
    os.path.join('Assets', 'PNG', 'Cars', 'car_green_5.png'))
car = pygame.transform.rotate(pygame.transform.scale(
    car_IMAGE, (car_WIDTH, car_HEIGHT)), 90)

# Border
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)

def draw_window(car_rect, car_image, car_health):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)  # Draw the border in black
    WIN.blit(car_image, (car_rect.x, car_rect.y))  # Draw car image at its position
    
    # Render and display health
    car_health_text = HEALTH_FONT.render("Health: " + str(car_health), 1, BLACK)
    WIN.blit(car_health_text, (10, 10))
    
    pygame.display.update()

def car_handle_movement(keys_pressed, car_rect):
    if keys_pressed[pygame.K_LEFT] and car_rect.x - VEL > BORDER.x + BORDER.width:  # LEFT
        car_rect.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and car_rect.x + VEL + car_rect.width < WIDTH:  # RIGHT
        car_rect.x += VEL
    if keys_pressed[pygame.K_UP] and car_rect.y - VEL > 0:  # UP
        car_rect.y -= VEL
    if keys_pressed[pygame.K_DOWN] and car_rect.y + VEL + car_rect.height < HEIGHT - 15:  # DOWN
        car_rect.y += VEL

def main():
    car_health = 5
    car_rect = pygame.Rect(50, HEIGHT // 2 - car_HEIGHT // 2, car_WIDTH, car_HEIGHT)  # Car position and size

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == CAR_HIT:
                car_health -= 1  # Decrease health when car is hit
               
                
        if car_health <=0:
            print("You lose!")


        # Handle car movement
        keys_pressed = pygame.key.get_pressed()
        car_handle_movement(keys_pressed, car_rect)

        # Draw everything
        draw_window(car_rect, car, car_health)
    
    pygame.quit()

if __name__ == "__main__":
    main()
