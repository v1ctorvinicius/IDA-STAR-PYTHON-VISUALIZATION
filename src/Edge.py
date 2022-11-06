import pygame as pg
import math

from Node import Node

import util.Colors as Colors

FONT = pg.font.Font('freesansbold.ttf', 32)

class Edge:
    def __init__(self, start: Node, end: Node, cost: int):
        self.start = start
        self.end = end
        self.cost = cost
        self.color = Colors.YELLOW
        self.costTextMesh = FONT.render(str(self.cost), True, Colors.BLACK, Colors.WHITE)

    def draw(self, display):
        pg.draw.line(display, self.color, self.start.getCenter(), self.end.getCenter(), 3)
        costTextRect = self.costTextMesh.get_rect()
        x_m_point = (self.start.getCenter()[0] + self.end.getCenter()[0]) / 2
        y_m_point = (self.start.getCenter()[1] + self.end.getCenter()[1]) / 2
        display.blit(self.costTextMesh, (x_m_point, y_m_point))
    