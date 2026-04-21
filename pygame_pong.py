import pygame  as pg
import random as r

win = pg.display.set_mode((0,0), pg.FULLSCREEN)
dims = win.get_size()

WHITE = (255, 255, 255)
pos = [200, 200]
radius = 50
gridsize = 50
c = [500, 500, 100]
color = [0, 0, 0]

def dist(x1, y1, x2, y2) -> bool:
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)

run = True
while run:
    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        if pos[1] > radius:
            pos[1] -= 1
    if keys[pg.K_a]:
        if pos[0] > radius:
            pos[0] -= 1
    if keys[pg.K_s]:
        if pos[1] < dims[1] - radius:
            pos[1] += 1
    if keys[pg.K_d]:
        if pos[0] < dims[0] - radius:
            pos[0] += 1

    # esemenykezeles
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if dist(c[0], c[1], event.pos[0], event.pos[1]) < c[2]:
                    c[0] = r.randint(c[2], dims[0] - c[2])
                    c[1] = r.randint(c[2], dims[1] - c[2])
                else:
                    pos = list(event.pos)
            if event.button == 3:
                color = [
                    r.randint(0, 255),
                    r.randint(0, 255),
                    r.randint(0, 255),
                ]
            if event.button == 4:
                # print('Fel gorgetes')
                radius += 5
            if event.button == 5:
                # print('Le gorgetes')
                if radius > 20:
                    radius -= 5
    # kirajzolas
    win.fill(WHITE)

    for x in range(0, dims[0], gridsize):
        for y in range(0, dims[1], gridsize):
            if (x // gridsize + y // gridsize) % 2 == 0:
                pg.draw.rect(win, (200, 200, 200), (x, y, gridsize, gridsize))

    pg.draw.circle(win, color, c[:2], c[2])
    pg.draw.circle(win, (255, 0, 0), pos, radius)

    # kepfrissites
    pg.display.flip()

pg.quit()