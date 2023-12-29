import pygame 
import copy
import random
class Snake:
    def __init__(self,rect):
       
        self.rect = rect
        self.direction = "RIGHT"


class Food:
    def __init__(self,rect): 
        self.rect = rect
    


class Game:
   
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.snake = Snake(pygame.Rect(300,300,20,20))
        self.screen = pygame.display.set_mode((width,height))
        self.snakes = list()
        self.snakes.append(self.snake)
        self.snakes.append(Snake(pygame.Rect(280,300,20,20)))
        self.snakes.append(Snake(pygame.Rect(260,300,20,20)))
        self.snakes.append(Snake(pygame.Rect(240,300,20,20)))
        self.food = Food(pygame.Rect(random.randint(20, width- 20),random.randint(20, height -20),20,20))
        self.score = 0
        
    def run(self):
        pygame.init()
        self.game_loop()
            
        pygame.quit()
        
       
    def game_loop(self) :
        running = True
        while running:
            
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_LEFT and self.snake.direction != "LEFT" and self.snake.direction != "RIGHT"):
                        self.snake.direction = "LEFT"
                       
                    elif (event.key == pygame.K_RIGHT and self.snake.direction != "LEFT" and self.snake.direction != "RIGHT"):
                         self.snake.direction = "RIGHT"
                    elif (event.key == pygame.K_DOWN and self.snake.direction != "DOWN" and self.snake.direction != "UP"):
                        self.snake.direction = "DOWN"
                    elif(event.key == pygame.K_UP and self.snake.direction != "DOWN" and self.snake.direction != "UP"):
                        self.snake.direction = "UP"

            # Fill the background with white
            self.screen.fill((255, 255, 255))

            # Draw a solid blue circle in the center
            pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
            self.draw_snake()
            if(self.game_over()):
                running = False
            pygame.time.delay(100)
            font = pygame.font.Font(None, 36)
            self.screen.blit( font.render("Score: "+ str(self.score), True, (0,0,0)), pygame.Rect(self.width-107, 0,50,50))
            # Flip the display
            pygame.display.flip()
            
            
    def draw_snake(self) :
        
        pygame.draw.rect(self.screen,(40,40,40),self.food.rect)
        for i  in range(len(self.snakes)) :
           
            pygame.draw.rect(self.screen,(40,40,40),rect = self.snakes[i].rect)
        self.update()
        
            
    def update_dot(self) :
        temp = copy.deepcopy(self.snakes)
            
        for i in range(1, len(self.snakes)):
            
            self.snakes[i].rect = temp[i-1].rect
    def update(self) :
        if(self.snake.direction == "UP"):
            self.snake.rect.y -= 20
        if(self.snake.direction == "DOWN"):
            self.snake.rect.y += 20
        if(self.snake.direction == "LEFT"):
            self.snake.rect.x -= 20
        if(self.snake.direction == "RIGHT"):
            self.snake.rect.x += 20
        if(self.snake.rect.x +20 < 0) :
            self.snake.rect.x = self.width -20
        if(self.snake.rect.x  > self.width):
            self.snake.rect.x = 0
        if(self.snake.rect.y +20 < 0) :
            self.snake.rect.y = self.height -20
        if(self.snake.rect.y  > self.height):
            self.snake.rect.y = 0
        if(self.snake.rect.colliderect(self.food.rect)):
            self.food.rect.x = random.randint(20,self.width-20)
            self.food.rect.y = random.randint(20,self.height-20)
            self.snakes.append(Snake(pygame.Rect(0,0,20,20)))
            self.score +=1
        self.update_dot()
    def game_over(self):
    
        print(len(self.snakes))
        for i in range(3,len(self.snakes)):
            if(self.snake.rect.colliderect(self.snakes[i].rect)) :
                return True
        return False

    
        
            