import pygame as pg

pg.init()
'''
win = pg.display.set_mode((1200, 900))
win.fill((255, 255, 255))
'''

'''
img = pg.image.load("image0.jpg")
res = pg.transform.scale(img, (460, 300)) # mit, mekkorara
rot = pg.transform.rotate(res, 45) # mit, mennyire
win.blit(img, (200, 200)) # mit, hova

pg.display.flip()
'''

'''
surf = pg.Surface((400, 400))
surf.fill((255, 0, 0))
pg.draw.circle(surf, (0, 0, 0), center=(50, 50), radius=150)

win.blit(surf, (150, 150))
pg.draw.circle(surf, (255, 255, 0), center=(50, 50), radius=20)
win.blit(surf, (50, 50))

pg.display.flip()
'''

'''
img = pg.transform.scale(pg.image.load('image0.jpg'), (460, 300))
surf = pg.Surface((460, 300))

for x in range(460):
    for y in range(300):
        color = img.get_at((x,y)) # (r,g,b)

        avg = (color[0] + color[1] + color[2]) / 3

        pg.draw.rect(surf, (avg, avg, avg), (x,y,1,1))
        

pg.image.save(surf, 'mod.jpg')
'''

'''
font = pg.font.SysFont('Arial', 72, True, False)
render = font.render('Hello World!', True, (0, 0, 0))
win.blit(render, (20, 20))

render = font.render('Hello World!', False, (0, 0, 0))
win.blit(render, (20, 200))

pg.display.flip()
'''

'''
rect = pg.Rect(200, 200, 350, 250)
print(rect.top) #top, left, bottom, right, topleft, bottomleft..., centerx, centery, center
rect.center = (600, 450)
print(rect.collidepoint(250, 250))
pg.draw.rect(win, (0, 0, 0), rect)
pg.display.flip()
'''

'''
fonts = (pg.font.get_fonts())
surf = pg.Surface((800, len(fonts) * 40))
surf.fill((255, 255, 255))

y = 0
for font in fonts:
    f = pg.font.SysFont(font, 36)
    render = f.render(font, True, (0, 0, 0))
    surf.blit(render, (20, y))
    y += 40

pg.image.save(surf, 'betuk.png')
'''

class Screen:
    def __init__(self):
        self.width = 1200
        self.height = 900
        self.size = (self.width, self.height)

        self.win = pg.display.set_mode(self.size)
        self.font = pg.font.SysFont('Arial', 72)
        self.run = True
        self.render = None
        self.text = ''

    def remake_render(self):
        self.render = self.font.render(self.text, True, (0, 0, 0))

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.remake_render()

    def draw(self):
        self.win.fill((255, 255, 255))
        if self.render:
            self.win.blit(self.render,(50, 50))
        pg.display.flip()
scr = Screen()
while scr.run:
    scr.event()
    scr.draw()

pg.quit()