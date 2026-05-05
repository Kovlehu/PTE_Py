import pygame as pg
import random as r

pg.init()

class Screen:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.dt = 0
        self.width = 800
        self.height = 800
        self.score_height = 50
        self.size = (self.width, self.height + self.score_height)
        self.win = pg.display.set_mode(self.size)
        self.games_played = 1
        self.font = pg.font.SysFont("Arial", 24)
        self.run = True
        self.active = False # nem indul el instant

        self.rows = 10
        self.snake = Snake(self.width, self.height, self.rows)
        self.apple = Apple(self.width, self.height, self.rows)

        self.last_move_time = pg.time.get_ticks()

    def reset_game(self):
        self.snake = Snake(self.width, self.height, self.rows)
        self.apple = Apple(self.width, self.height, self.rows)
        self.active = False
        self.games_played += 1
        self.last_move_time = pg.time.get_ticks()

    def iterate(self):
        self.event()

        if self.active:
            current_time = pg.time.get_ticks()
            if current_time - self.last_move_time > 500:
                head = self.snake.body[0]

                if head in self.snake.body[1:]:
                    self.reset_game()
                    return

                eat = False
                if head[0] == self.apple.x and head[1] == self.apple.y:
                    eat = True
                    self.apple.spawn(self.snake.body)

                self.snake.move(grow = eat)
                self.last_move_time = current_time

        self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

            # start gomb
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.active = True

            # controls
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w and self.snake.dir != (0, 1):
                    self.snake.dir = (0, -1)
                if event.key == pg.K_s and self.snake.dir != (0, -1):
                    self.snake.dir = (0, 1)
                if event.key == pg.K_a and self.snake.dir != (1, 0):
                    self.snake.dir = (-1, 0)
                if event.key == pg.K_d and self.snake.dir != (-1, 0):
                    self.snake.dir = (1, 0)

    def draw(self):
        self.win.fill((255, 255, 255))

        # mezok
        for i in range(self.rows + 1):
            line_pos = i * (self.width // self.rows)
            pg.draw.line(self.win, (0, 0, 0), (line_pos, 0), (line_pos, self.height))
            pg.draw.line(self.win, (0, 0, 0), (0, line_pos), (self.width, line_pos))

        # render
        self.apple.draw(self.win)
        self.snake.draw(self.win)

        # lenti UI
        lenght_text = self.font.render(f"Hossz: {len(self.snake.body)}", True, (0, 0, 0))
        games_text = self.font.render(f"Jatekok: {self.games_played}", True, (0, 0, 0))

        self.win.blit(lenght_text, (20, self.height + 10))
        self.win.blit(games_text, (200, self.height + 10))

        if not self.active:
            msg = "Nyomj SPACE-t az inditashoz!" if self.games_played == 1 else "Jatek vege! SPACE az ujrainditashoz"
            overlay = self.font.render(msg, True, (255, 0, 0))
            self.win.blit(overlay, (self.width // 2 - 120, self.height // 2))

        pg.display.flip()

class Snake:
    def __init__(self, screen_width, screen_height, rows):
        self.size = screen_width // rows
        self.rows = rows
        # random starthely
        start_x = r.randint(3, rows - 3) * self.size
        start_y = r.randint(3, rows - 3) * self.size
        # random startirany
        self.dir = r.choice([(1, 0), (-1, 0), (0, -1), (0, 1)])
        # test lista
        self.body = [
            [start_x, start_y],
            [start_x - self.size, start_y],
            [start_x - (2 * self.size), start_y],
        ]

        self.color = (0, 51, 0)

    def move(self, grow = False):
        # uj fej helye
        curr_head = self.body[0]
        new_head = [
            (curr_head[0] + (self.dir[0] * self.size)) % (self.rows * self.size),
            (curr_head[1] + (self.dir[1] * self.size)) % (self.rows * self.size),
        ]
        # wrap around
        new_head[0] %= (self.rows * self.size)
        new_head[1] %= (self.rows * self.size)
        # uj fej lista elejere
        self.body.insert(0, new_head)
        # ha alma akkor grow, amugy pop
        if not grow:
            self.body.pop()

    def draw(self, surface):
        for index, segment in enumerate(self.body):
            shape = pg.Rect(segment[0], segment[1], self.size, self.size)

            # fejnek mas szin
            if index == 0:
                head_color = (0, 100, 0)
                pg.draw.rect(surface, head_color, shape)
            else:
                pg.draw.rect(surface, self.color, shape)

            pg.draw.rect(surface, (0, 255, 0), shape, 1)

class Apple:
    def __init__(self, screen_width, screen_height, rows):
        self.size = screen_width // rows
        self.rows = rows
        self.spawn()

    def spawn(self, snake_body = []):
        invalid_pos = True

        while invalid_pos:
            self.x = r.randint(0, self.rows - 1) * self.size
            self.y = r.randint(0, self.rows - 1) * self.size

            if [self.x, self.y] not in snake_body:
                invalid_pos = False

    def draw(self, surface):
        pg.draw.rect(surface, (180, 0, 0), (self.x, self.y, self.size, self.size))

scr = Screen()
while scr.run:
    scr.iterate()

pg.quit()