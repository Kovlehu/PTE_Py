import pygame as pg

class Screen:
    def __init__(self):
        self.width = 1200
        self.height = 900
        self.size = (self.width, self.height)

        self.win = pg.display.set_mode(self.size)
        self.run = True

    def iterate(self):
        self.iterate()
        self.draw

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def draw(self):
        self.win.fill((0, 0, 0))

        pg.display.flip()