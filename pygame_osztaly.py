import pygame as pg
import random as r

class Screen:
    def __init__(self):
        self.width = 1000
        self.height = 800
        self.size = (self.width, self.height)

        self.win = pg.display.set_mode(self.size)
        self.run = True

        self.paddles = [
            Paddle([20, 250], self.size, pg.K_w, pg.K_s),
            Paddle([self.width - 20, 250], self.size, pg.K_UP, pg.K_DOWN),
        ]

        self.ball = Ball(
            [self.width//2, self.height//2],
            [r.choice([1, -1]), r.choice([1, -1])],
            self.paddles,
            self.size
        )

    def iterate(self):
        self.event()
        self.ball.iterate()
        self.draw()

    def event(self):
        for paddle in self.paddles:
            paddle.event()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def draw(self):
        self.win.fill((0, 0, 0))
        for paddle in self.paddles:
            paddle.draw(self.win)
        self.ball.draw(self.win)

        pg.display.flip()

class Paddle:
    def __init__(self, pos, screensize,  up, down):
        self.pos = pos
        self.screensize = screensize
        self.up = up
        self.down = down

        self.height = 150
        self.width = 8

        self.speed = 0.35

    def event(self):
        keys = pg.key.get_pressed()
        if keys[self.up]:
            self.pos[1] -= self.speed
        if keys[self.down]:
            self.pos[1] += self.speed

        if self.pos[1] < 0:
            self.pos[1] = 0
        if self.pos[1] > self.screensize[1] - self.height:
            self.pos[1] = self.screensize[1] - self.height

    def draw(self, win):
        endpos = [self.pos[0], self.pos[1] + self.height]
        pg.draw.line(win, (255, 255, 255), self.pos, endpos, self.width)

class Ball:
    def __init__(self, pos, movement, paddles, screensize):
        self.pos = pos
        self.movement = movement # [1, -1], ...
        self.paddles = paddles
        self.screensize = screensize

        self.speed = 0
        self.radius = 20

    def iterate(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.speed = 0.25
        # movement vector es speed segitsegevel self.pos-t valtoztatja
        self.pos[0] += self.movement[0] * self.speed
        self.pos[1] += self.movement[1] * self.speed
        # ha szelen van visszapattan
        if self.pos[1] < self.radius: # fent
            self.movement[1] = 1
        if self.pos[0] < self.radius: # balra
            self.movement[0] = 1
            return False
        if self.pos[1] > self.screensize[1] - self.radius: # lent
            self.movement[1] = -1
        if self.pos[0] > self.screensize[0] - self.radius: # jobbra
            self.movement[0] = -1
            return False

        x,y = self.pos
        l_paddle_bottom = self.paddles[1].pos[1] + self.paddles[0].height
        r_paddle_bottom = self.paddles[1].pos[1] + self.paddles[0].height

        if x - self.radius < self.paddles[0].pos[0]:
            if y > self.paddles[0].pos[1] and y < l_paddle_bottom:
                self.movement[0] = 1

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