import pygame
import sys
from settings import *
import random
from PIL import Image

class Start():
    def __init__(self,screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.img = Image.open("start.gif")
        self.frames = []
        self.load_frames()
        self.frames_count = len(self.frames)
        self.current_frame = 0

    def load_frames(self):
        try:
            while True:
                frame = self.img.copy()
                frame = frame.convert("RGBA")  # In RGBA konvertieren
                frame = frame.resize((1280, 720), Image.LANCZOS)  # Auf Fenstergröße anpassen
                self.frames.append(pygame.image.fromstring(frame.tobytes(), frame.size, frame.mode))
                print(f"Frame {len(self.frames)} loaded with size: {frame.size}")  # Debugging-Ausgabe
                self.img.seek(len(self.frames))  # Zum nächsten Frame wechseln
        except EOFError:

            print("All frames loaded")  # Debugging-Ausgabe


    def update(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        run = False
                    if event.key == pygame.K_ESCAPE:
                        run = False
            
            if self.frames_count > 0:
                self.screen.blit(self.frames[self.current_frame] ,(0,0))
                self.current_frame = (self.current_frame + 1) % self.frames_count


            self.clock.tick(FPS)
            pygame.display.update()
        
class Food():
    def __init__(self,screen,snake):
        self.food_block = 40
        self.screen = screen
        self.snake = snake
        self.food_x = random.randint(0, (WIDTH // self.food_block) - 1) * self.food_block 
        self.food_y = random.randint(0, (HEIGHT // self.food_block) - 1) * self.food_block 
    def update(self):
        self.food = pygame.draw.rect(self.screen,"orange",(self.food_x,self.food_y,self.food_block,self.food_block))
        
    def check_collision(self):
        snake_head = self.snake.snake_list[-1]
        #print(f"Snake head: {snake_head}, Futterposition: ({self.food_x},{self.food_y})") debugging
        if self.snake.snake.colliderect(self.food):
            return True
        return False

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("Snake")
        self.snake = Snake(0,0,self.screen)
        self.food = Food(self.screen,self.snake)
        self.start = Start(self.screen)
        self.font = pygame.font.Font("Minecraftia.ttf",20)
        self.score = 0
        self.start.update() 
    def update(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.start.update()

            self.screen.fill("darkgreen")
            self.snake.update()
            self.food.update()

            if self.food.check_collision():
                self.score += 1
                self.snake.snake_len += 2
                self.food.food_x = random.randint(0,1000)
                self.food.food_y = random.randint(0,500)

            self.format_score = str(self.score).zfill(5)
            self.score_text = self.font.render(self.format_score,True,"white")
            self.screen.blit(self.score_text,(10,0))
            pygame.display.update()
            self.clock.tick(FPS)

class Snake():
    def __init__(self,x,y,screen):
        pygame.init()

        self.snake_block = 40
        self.snake_x = x
        self.snake_y = y
        self.snake_speed = 6
        
        self.snake_list = []
        self.snake_len = 1

        self.direction = "RIGHT"
        self.change_to = self.direction
        self.screen = screen

 
        self.snake_head = [self.snake_x,self.snake_y]
        self.snake_list.append(self.snake_head)   

           
   
        
    def update(self):
        self.direction = self.change_to
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.change_to = "UP"
        if pressed[pygame.K_s]:
            self.change_to = "DOWN"
        if pressed[pygame.K_d]:
            self.change_to = "RIGHT"
        if pressed[pygame.K_a]:
            self.change_to  = "LEFT"


        if self.change_to == "RIGHT":
            self.snake_x += self.snake_speed
        elif self.change_to == "LEFT":
            self.snake_x -= self.snake_speed
        elif self.change_to == "UP":
            self.snake_y -= self.snake_speed
        elif self.change_to == "DOWN":
            self.snake_y += self.snake_speed


        self.snake_list.append((self.snake_x,self.snake_y))
        if len(self.snake_list) > self.snake_len:
            del self.snake_list[0]

        for i in self.snake_list:
            self.snake = pygame.draw.rect(self.screen,"green",(i[0],i[1],self.snake_block,self.snake_block))

        for body in self.snake_list[:-1]:
            if body == self.snake_head:
                sys.exit(0)
      
        if self.snake_x > 1240 or self.snake_x < 0:
            sys.exit(0)
        if self.snake_y > 670 or self.snake_y < 0:
            sys.exit(0)

if __name__ == "__main__":
    game = Game()
    game.update()
    


