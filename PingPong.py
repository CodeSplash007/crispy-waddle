import pygame

CLOCK = pygame.time.Clock()
FPS = 60

WIDTH, HEIGHT = 1000, 600
PLAYER_WIDTH, PLAYER_HEIGHT = 10, 100

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def red_player_move(red_player, keys):
    if keys[pygame.K_w]:
        red_player.y -= 5

    if keys[pygame.K_s]:
        red_player.y += 5

def draw(RED_PLAYER, BLUE_PLAYER):
    WIN.fill("white")
    pygame.draw.rect(WIN, "red", RED_PLAYER)
    pygame.draw.rect(WIN, "blue", BLUE_PLAYER)
    pygame.display.update()

def main():
    run = True

    RED_PLAYER = pygame.Rect(10, 10,PLAYER_WIDTH, PLAYER_HEIGHT)
    BLUE_PLAYER = pygame.Rect(WIDTH - PLAYER_WIDTH - 10, 10, PLAYER_WIDTH, PLAYER_HEIGHT)

    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw(RED_PLAYER, BLUE_PLAYER)

        keys_pressed = pygame.key.get_pressed()

        red_player_move(RED_PLAYER, keys_pressed)



if __name__ == "__main__":
    main()