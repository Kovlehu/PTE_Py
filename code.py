import pygame
import time

class Screen:
    def __init__(self):
        self.size = (1500, 900)
        self.win = pygame.display.set_mode(self.size)

        self.run = True
        self.character = Character([self.size[0]/2, self.size[1]/2])

        self.last_time = time.time()

    def iterate(self):
        current = time.time()
        dt = current - self.last_time
        self.last_time = current

        # if dt > 0:
        #     print(1 / dt)

        self.event(dt)
        self.character.iterate()
        self.draw()

    def event(self, dt):
        self.character.event(dt)
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
        self.direction = 0
        self.speed = 200
        self.moving = False
        self.load_graphics()

        self.animation_frame = 0
        self.animation_fps = 10
        self.animation_last_time = None

    def iterate(self):
        if not self.moving:
            self.animation_frame = 0
            self.animation_time = None
        else:
            if self.animation_last_time is None:
                self.animation_last_time = time.time()
            else:
                current = time.time()
                diff = current - self.animation_last_time
                if diff > 1 / self.animation_fps:
                    self.animation_frame += 1
                    self.animation_last_time += 1 / self.animation_fps

    def load_graphics(self):
        self.graphics = {}
        for direction in range(8):
            self.graphics[direction] = {
                "idle": pygame.image.load(f"Human/Male_{direction}_Idle0.png"),
                "run": []
            }
            for frame in range(10):
                img = pygame.image.load(f"Human/Male_{direction}_Run{frame}.png")
                self.graphics[direction]["run"].append(img)

        print(self.graphics)

    def event (self, dt):
        keys = pygame.key.get_pressed()
        w, a, s, d = pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d

        self.moving = True
        if keys[w] and keys[a]:
            self.direction = 6
        elif keys[w] and keys[d]:
            self.direction = 0
        elif keys[s] and keys[a]:
            self.direction = 4
        elif keys[s] and keys[d]:
            self.direction = 2
        elif keys[w]:
            self.direction = 7
        elif keys[a]:
            self.direction = 5
        elif keys[s]:
            self.direction = 3
        elif keys[d]:
            self.direction = 1
        else:
            self.moving = False

        if self.moving:
            movement = pygame.math.Vector2(1, -1).rotate(self.direction * 45)
            movement.scale_to_length(self.speed)

            self.pos[0] += movement[0] * dt
            self.pos[1] += movement[1] * dt

    def draw(self, win):
        # pygame.draw.circle(win, (0, 0, 0), self.pos, 20)
        if not self.moving:
            win.blit(self.graphics[self.direction]["idle"], self.pos)
        else:
            li = self.graphics[self.direction]["run"]
            win.blit(li[self.animation_frame % len(li)], self.pos)

scr = Screen()
while scr.run:
    scr.iterate()

pygame.quit()