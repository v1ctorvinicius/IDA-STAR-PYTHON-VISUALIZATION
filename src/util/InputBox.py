import pygame as pg
from util import Colors

COLOR_INACTIVE = Colors.LIGHT_BLUE
COLOR_ACTIVE = Colors.RED

pg.init()
FONT = pg.font.Font('freesansbold.ttf', 32)

class InputBox:
    def __init__(self, x, y, w, h, text = ''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handleEvent(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        
        self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE

        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

            self.txt_surface = FONT.render(self.text, True, self.color)

    def draw(self, display):
        display.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(display, self.color, self.rect, 2)