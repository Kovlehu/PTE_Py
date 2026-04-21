import pygame
import time

class Screen:
    def __init__(self):
        self.size = (1500, 900)
        self.win = pygame.display.set_mode(self.size)

        self.run = True
        self.character = Character((self.size[0]/2, self.size[1]/2))

        self.last_time = time.time()

    def iterate(self):
        current = time.time()
        dt = current - self.last_time
        self.last_time = current

        print(dt)

        self.event()
        self.draw()

    def event(self):
        self.character.event()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def draw(self):
        self.win.fill((255,255,255))
        self.character.draw(self.win)
        pygame.display.flip()

class Character:
    def __init__(self, pos):
        self.pos = pos

    def event (self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos[1] -= 1
        if keys[pygame.K_a]:
            self.pos[0] -= 1
        if keys[pygame.K_s]:
            self.pos[1] += 1
        if keys[pygame.K_d]:
            self.pos[0] += 1

    def draw(self, win):
        pygame.draw.circle(win, (0, 0, 0), self.pos, 20)

scr = Screen()
while scr.run:
    scr.iterate()

pygame.quit()







