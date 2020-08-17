import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 0
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 690
paddleB.rect.y = 200

ball = Ball(10, 10, WHITE)
ball.rect.x = 350
ball.rect.y = 200

size = (700, 500)
window = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

clock = pygame.time.Clock()

run = True

scoreA = 0
scoreB = 0

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddleA.move_up(5)
    if keys[pygame.K_s]:
        paddleA.move_down(5)
    if keys[pygame.K_UP]:
        paddleB.move_up(5)
    if keys[pygame.K_DOWN]:
        paddleB.move_down(5)

    all_sprites_list.update()

    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]

    if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
        ball.bounce()

    window.fill(BLACK)
    pygame.draw.line(window, WHITE, (350, 0), (350, 500), 5)
    all_sprites_list.draw(window)

    font = pygame.font.Font(None, 50)
    text = font.render(str(scoreA), 1, WHITE)
    window.blit(text, (175, 20))
    text = font.render(str(scoreB), 1, WHITE)
    window.blit(text, (525, 20))

    pygame.display.flip()

pygame.quit()
