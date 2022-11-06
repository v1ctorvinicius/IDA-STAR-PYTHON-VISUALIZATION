import pygame as pg
import util.Colors as Colors

class PlusButton():
    def __init__(self, x: int, y: int):
        self.icon = pg.image.load('img/plus.png').convert_alpha()
        self.rect = self.icon.get_rect()
        self.x = x - self.rect.width // 2
        self.y = y - self.rect.height // 2


        # self.text = ''
        # self.font = pg.font.SysFont('cambria', 50)
        # self.rect.topleft = (x, y)
        # width = self.icon.get_width()
        # height = self.icon.get_height()

    def draw(self, display: pg.Surface):
        display.blit(self.icon, (self.x, self.y))

    def checkInputDown(self, pos):
        if pos[0] in range(self.x , self.x + self.rect.width) and pos[1] in range(self.y, self.y + self.rect.height):
            return True
            