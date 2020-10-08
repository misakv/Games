import random

class State:
    def __init__(self):
        #rozmistime jidlo nahodne
        self.food = []
        self.add_food()
        self.add_food()

        self.snake = [(0, 0), (1, 0)]  
        self.snake_direction = 0, 1
        self.width = 10
        self.height = 10
        self.snake_alive = True

    def move(self):
        if not self.snake_alive:
            return

        dir_x, dir_y = self.snake_direction
        old_x, old_y = self.snake[-1]
        new_x = old_x + dir_x
        new_y = old_y + dir_y

        #kontrola vylezení z hrací plochy
        if new_x < 0 or new_x >= self.width or new_y < 0 or new_y >= self.height :
            exit('GAME OVER')
            
        new_head = new_x, new_y
        self.snake.append(new_head)
        
        #had nesmi narazit sam do sebe
        if new_head in self.snake:
            self.snake_alive = False


        #had sezere jablko a vyroste
        if new_head in self.food:
            self.food.remove(new_head)
            self.add_food()
        else:
            del self.snake[0]

    def add_food(self):
        pridano = False

        while not pridano:  #musi se vzdycky pridat jidlo
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            position = x, y

            #nepridavat jidlo kdyz je na policku telo hada nebo jine jidlo
            if (position not in self.snake) and (position not in self.food):
                self.food.append(position)
                pridano = True
                return