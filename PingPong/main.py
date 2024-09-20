import pygame
import sys
from settings import *
import random



class Game():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("PingPong")
        self.gameover = Gameover()
        self.player = Player(500,600,self.gameover)
    def update(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
            
            self.screen.fill("black")
            self.player.update(self.screen,)
            pygame.display.update()
            self.clock.tick(FPS)

class Player():
    def __init__(self,x,y,gameover):
        self.player_x = x
        self.player_y = y
        self.player_speed = 10

        self.ball_x = random.randint(0,1000) 
        self.ball_y = random.randint(0,200)
        self.ball_speed_x = 4
        self.ball_speed_y = 5
        self.ball_dx = -1
        self.ball_dy = -1

        self.score = 0
        self.font = pygame.font.Font("/root/nvim/stuff/PingPong/Minecraftia.ttf",20)


        self.paddle_sound = pygame.mixer.Sound("paddle.mp3")
        self.wall_sound = pygame.mixer.Sound("wall.mp3")
        self.paddle_sound.set_volume(0.1)
        self.wall_sound.set_volume(0.1)

        self.gameover = gameover
    def reset_ball(self):
        self.ball_x = random.randint(0,1000)
        self.ball_y = random.randint(0,200)

    def update(self,screen):
        # get key input 
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_d]:
            self.player_x += self.player_speed
        elif pressed[pygame.K_a]:
            self.player_x -= self.player_speed

        # screen collision player
        if self.player_x > 1170:
            self.player_x = 1170 
        elif self.player_x < 0:
            self.player_x = 0
        
        self.ball_y += self.ball_speed_y
        self.ball_x += self.ball_speed_x

        self.player = pygame.draw.rect(screen,"white",(self.player_x,self.player_y,120,20))
        self.ball = pygame.draw.ellipse(screen,"yellow",(self.ball_x,self.ball_y,30,30))

        if self.player.colliderect(self.ball):
            self.ball_speed_y *= self.ball_dy
            self.score += 1
            self.paddle_sound.play()
                

        # screen collision ball
        if self.ball_y > 680 or self.ball_y < 0:
            self.ball_speed_y *= self.ball_dy
            self.wall_sound.play()
        if self.ball_x > 1240 or self.ball_x < 0:
            self.ball_speed_x *= self.ball_dx
            self.wall_sound.play()


        if self.score < 0:
            self.score = 0

        if self.ball_y > 680:
            self.score = 0
            self.gameover.update()
            self.reset_ball()
         
        self.format_score = str(self.score).zfill(5)

        self.score_text = self.font.render(self.format_score,True,"white")
        game.screen.blit(self.score_text,(10,0))



class Gameover():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("Minecraftia.ttf",30)
    def update(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                        run = False

            self.text_surface = self.font.render("Game Over",True,"red")
            game.screen.fill("black")
            game.screen.blit(self.text_surface,(WIDTH // 2 - self.text_surface.get_width() // 2 ,HEIGHT // 2 - self.text_surface.get_height() // 2))

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.update()
    
