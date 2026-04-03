import pygame as pg
import random as r

pg.init()
pg.font.init()

class Screen:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.dt = 0
        self.width = 1200
        self.height = 900
        self.score_height = 100
        self.size = (self.width, self.height)

        self.scores = [0, 0]
        self.font = pg.font.SysFont("Arial", 50)

        self.win = pg.display.set_mode(self.size)
        self.run = True

        self.paddles = [
            Paddle([20, 250], self.size, pg.K_w, pg.K_s, self.score_height),
            Paddle([self.width - 20, 250], self.size, pg.K_UP, pg.K_DOWN, self.score_height),
        ]

        self.ball = Ball(
            [self.width//2, self.height//2],
            [r.choice([1, -1]), r.choice([1, -1])],
            self.paddles,
            self.size,
            self.score_height
        )

    def iterate(self):
        self.dt = self.clock.tick(60) /1000.0
        self.event(self.dt)

        result = self.ball.iterate(self.dt)

        if result == "BAL":
            self.scores[0] += 1
            self.reset_ball()
        elif result == "JOBB":
            self.scores[1] += 1
            self.reset_ball()

        self.draw()

    def reset_ball(self):
        self.ball.pos = [self.width // 2, (self.height + self.score_height) // 2]
        self.ball.speed = 0

    def event(self, dt):
        for paddle in self.paddles:
            paddle.event(dt)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def draw(self):
        self.win.fill((0, 0, 0))

        score_text = f"{self.scores[0]}     |     {self.scores[1]}"
        img = self.font.render(score_text, True, (255, 255, 255))
        self.win.blit(img, (self.width // 2 - img.get_width() // 2, 20))

        play_rect = (0, self.score_height, self.width, self.height - self.score_height)
        pg.draw.rect(self.win, (255, 255, 255), play_rect, 2)

        for paddle in self.paddles:
            paddle.draw(self.win)
        self.ball.draw(self.win)

        for y in range(self.score_height, self.height, 40):
            pg.draw.rect(self.win, (211, 211, 211), (self.width // 2 - 2, y, 4, 20))

        pg.display.flip()

class Paddle:
    def __init__(self, pos, screensize, up, down, y_offset):
        self.pos = pos
        self.screensize = screensize
        self.y_offset = y_offset
        self.up = up
        self.down = down

        self.height = 150
        self.width = 8

        self.speed = 500

    def event(self, dt):
        keys = pg.key.get_pressed()
        if keys[self.up]:
            self.pos[1] -= self.speed * dt
        if keys[self.down]:
            self.pos[1] += self.speed * dt

        if self.pos[1] < self.y_offset:
            self.pos[1] = self.y_offset
        if self.pos[1] > self.screensize[1] - self.height:
            self.pos[1] = self.screensize[1] - self.height

    def draw(self, win):
        endpos = [self.pos[0], self.pos[1] + self.height]
        pg.draw.line(win, (255, 255, 255), self.pos, endpos, self.width)

class Ball:
    def __init__(self, pos, movement, paddles, screensize, y_offset):
        self.pos = pos
        self.movement = movement # [1, -1], ...
        self.paddles = paddles
        self.screensize = screensize
        self.y_offset = y_offset

        self.speed = 0
        self.radius = 20

    def iterate(self, dt):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.speed = 400
        # movement vector es speed segitsegevel self.pos-t valtoztatja
        self.pos[0] += self.movement[0] * self.speed * dt
        self.pos[1] += self.movement[1] * self.speed * dt
        # ha szelen van visszapattan
        if self.pos[1] < self.y_offset + self.radius: # fent
            self.movement[1] = 1
        if self.pos[0] < self.radius: # balra
            self.movement[0] = 1
            return "JOBB"
        if self.pos[1] > self.screensize[1] - self.radius: # lent
            self.movement[1] = -1
        if self.pos[0] > self.screensize[0] - self.radius: # jobbra
            self.movement[0] = -1
            return "BAL"

        x,y = self.pos
        l_paddle_bottom = self.paddles[0].pos[1] + self.paddles[0].height
        r_paddle_bottom = self.paddles[1].pos[1] + self.paddles[1].height

        if x - self.radius < self.paddles[0].pos[0] + self.paddles[0].width:
            if y > self.paddles[0].pos[1] and y < l_paddle_bottom:
                self.movement[0] = 1
                self.pos[0] = self.paddles[0].pos[0] + self.paddles[0].width + self.radius

        if x + self.radius > self.paddles[1].pos[0]:
            if y > self.paddles[1].pos[1] and y < r_paddle_bottom:
                self.movement[0] = -1
        return True

    def draw(self, win):
        # self.pos helyere self.radius meretu kort rajzol
        pg.draw.circle(win, (255, 255, 255), self.pos, self.radius)

scr = Screen()
while scr.run:
    scr.iterate()

pg.quit()