import pygame
import os
pygame.font.init()
pygame.mixer.init()
 
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
 

 
FPS = 60
VEL = 5
car_WIDTH, car_HEIGHT = 55, 40
 

HEALTH_FONT = pygame.font.SysFont("helvetica", 30)
CAR_HIT = pygame.USEREVENT + 1  # Define custom event for car hit

# Load and scale images
car_IMAGE = pygame.image.load(
    os.path.join('Assets', 'PNG', 'Cars', 'car_green_5.png'))
car = pygame.transform.rotate(pygame.transform.scale(
    car_IMAGE, (car_WIDTH, car_HEIGHT)), 90)
 
BACKGROUND = pygame.transform.scale(
    pygame.image.load(os.path.join('Assets', 'PNG', 'Tiles', 'Asphalt road', 'road_asphalt01.png')),(WIDTH, HEIGHT)
)
 
def draw_window(car_rect, car_health):
    WIN.blit(BACKGROUND, (0, 0))  # Draw the background first
    WIN.blit(car, (car_rect.x, car_rect.y))  # Draw car image at its position

    car_health_text = HEALTH_FONT.render("Health: " + str(car_health), 1, BLACK)
    WIN.blit(car_health_text, (10, 10))

    pygame.display.update()
 
def car_handle_movement(keys_pressed, car_rect):
    if keys_pressed[pygame.K_LEFT] and car_rect.x - VEL > 0:  # LEFT
        car_rect.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and car_rect.x + VEL + car_rect.width < WIDTH:  # RIGHT
        car_rect.x += VEL
    if keys_pressed[pygame.K_UP] and car_rect.y - VEL > 0:  # UP
        car_rect.y -= VEL
    if keys_pressed[pygame.K_DOWN] and car_rect.y + VEL + car_rect.height < HEIGHT - 15:  # DOWN
        car_rect.y += VEL
 
def main():
    car_health = 5
    car_rect = pygame.Rect(100, 300, car_WIDTH, car_HEIGHT)  # Initialize car position
    clock = pygame.time.Clock()
    run = True
 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == CAR_HIT:
                car_health -= 1  # Decrease health when car is hit

        keys_pressed = pygame.key.get_pressed()
        car_handle_movement(keys_pressed, car_rect)
        draw_window(car_rect, car_health)  # Draw everything in each frame
 
main()    
 
if __name__ == "__main__":
    main()