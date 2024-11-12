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
BLACK = (0, 0, 0)


BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

FPS = 60
VEL = 5
car_WIDTH, car_HEIGHT = 55, 40

car_IMAGE = pygame.image.load(
    os.path.join('Assets', 'PNG', 'Cars', 'car_green_5.png'))
car = pygame.transform.rotate(pygame.transform.scale(
    car_IMAGE, (car_WIDTH, car_HEIGHT)), 90)


def draw_window(car_rect, car_image):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)  # Draw the border in black
    WIN.blit(car_image, (car_rect.x, car_rect.y))  # Draw car image at its position
    pygame.display.update()

def car_handle_movement(keys_pressed, car):
    if keys_pressed[pygame.K_LEFT] and car.x - VEL > BORDER.x + BORDER.width:  # LEFT
        car.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and car.x + VEL + car.width < WIDTH:  # RIGHT
        car.x += VEL
    if keys_pressed[pygame.K_UP] and car.y - VEL > 0:  # UP
        car.y -= VEL
    if keys_pressed[pygame.K_DOWN] and car.y + VEL + car.height < HEIGHT - 15:  # DOWN
        car.y += VEL

def main():

    car_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


    keys_pressed = pygame.key.get_pressed()
    car_handle_movement(keys_pressed, car)
    draw_window(car, car_health)

    main()


if __name__ == "__main__":
    main()