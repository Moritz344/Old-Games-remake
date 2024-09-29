import pygame
import random
import time
# TODO: SFX
pygame.init()

x = 800
y = 600
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("pong")
clock = pygame.time.Clock()

# game variablen
player_pos_x = 200
player_pos_y = 300
player_speed = 7

player_x_2 = 600
player_y_2 = 300
player_speed_2 = 7
react_time = random.uniform(1, 3)
print("Computer Reaction time:", react_time)

ball_size = 10
ball_pos_x = x // 2
ball_pos_y = player_pos_y // 2
ball_speed_x = 5
ball_speed_y = 5

# Score System
score_1 = 0
score_2 = 0

# TEXT
pygame.font.init()
font = pygame.font.SysFont("Open Sans", 50)
text_farbe = (255, 255, 255)

# farben
weiss = (255, 255, 255)
dark_grey = (0, 0, 0)
blue = (15, 82, 186)

# Retro Neon
dark_blue = (0, 0, 139)
neon_grün = (57, 255, 20)
neon_pink = (255, 20, 147)

# Weltraum
black = (0, 0, 0)
sternen_weiß = (237, 237, 237)
glow_blue = (30, 144, 255)

# SFX
paddle_sound = pygame.mixer.Sound("paddle.mp3")
wall_sound = pygame.mixer.Sound("wall.mp3")
paddle_sound.set_volume(0.1)
wall_sound.set_volume(0.1)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.update()
            run = False

    screen.fill(dark_blue)

    player = pygame.draw.rect(screen, neon_grün,
                              [player_pos_x, player_pos_y, 10, 50])
    player_2 = pygame.draw.rect(screen, neon_grün,
                                [player_x_2, player_y_2, 10, 50])

    ball = pygame.draw.ellipse(screen, weiss,
                               [ball_pos_x, ball_pos_y, ball_size, ball_size])

    def func_netz():
        netz_pos_x = x // 2
        netz_pos_y = -6
        netz_1 = pygame.draw.rect(screen, weiss,
                                  [netz_pos_x, netz_pos_y, 10, 30])

        for i in range(1, 8):
            netz_pos_y = i * 100
            pygame.draw.rect(screen, weiss, [netz_pos_x, netz_pos_y, 10, 30])

    # ball
    if ball_pos_x < 0 or ball_pos_x > x:
        wall_sound.play()
        ball_speed_x *= -1
    if ball_pos_y < 0 or ball_pos_y > y:
        wall_sound.play()
        ball_speed_y *= -1

    if ball_pos_x < 0:
        score_2 += 1
        print("Punkt für Spieler_2:", score_2)
    elif ball_pos_x > x:
        score_1 += 1
        print("Punkt für Spieler 1:", score_1)

    if score_2 >= 5 or score_1 >= 5:
        score_2 = 0
        score_1 = 0

    if score_1 > score_2:
        react_time = max(1, react_time - 0.1)
    else:
        react_time = min(10, react_time + 0.1)

    # drawing the Text
    def drawing_text():
        text_surface = font.render(f"{score_1}", False, (255, 255, 255))
        text_surface_2 = font.render(f"{score_2}", False, (255, 255, 255))

        screen.blit(text_surface, (200, 0))
        screen.blit(text_surface_2, (600, 0))

    if ball.colliderect(player):
        paddle_sound.play()
        ball_speed_x = -ball_speed_x

    elif ball.colliderect(player_2):
        paddle_sound.play()
        ball_speed_x = -ball_speed_x

    ball_pos_y += ball_speed_y
    ball_pos_x += ball_speed_x

    # Keyboard Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos_y -= player_speed
    elif keys[pygame.K_s]:
        player_pos_y += player_speed

    # collision Player 1
   if player_pos_y < 0:
       player_pos_y = 0
   elif player_pos_y > 560:
         player_pos_y = 560
 
    # collision Player 2
    if player_y_2 < 0:
      player_y_2 = 0
    elif player_y_2 > 560:
          player_y_2 = 560
 
 
      # Player_2
      # KI für den zweiten Spieler
    if ball_pos_x > x // 2:  # Wenn der Ball auf die Seite des Computers kommt
      if ball_pos_y < player_y_2 - react_time:  # Paddle nach oben bewegen
        player_y_2 -= player_speed_2
      elif ball_pos_y > player_y_2 + react_time:  # Paddle nach unten bewegen
           player_y_2 += player_speed_2
 
      if ball_pos_x > player_x_2: # ball ist hinter Paddle
          react_time += 1
      else:
             react_time = 10
 
          # react_time = max(1,react_time - 0.1)
          # react_time = min(10,react_time + 0.1)

    drawing_text()
    func_netz()
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()
   
