import pygame as pg

class Screen:
    def __init__(self):
        self.clock = pg.time.Clock()
        self.dt = 0
        self.width = 1200
        self.height = 900
        self.size = (self.width, self.height)

        self.win = pg.display.set_mode(self.size)
        self.run = True

    def iterate(self):
        self.dt = self.clock.tick(60) / 1000.0
        self.event(self.dt)

        self.draw

    def event(self, dt):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def draw(self):
        self.win.fill((0, 0, 0))

        pg.display.flip()