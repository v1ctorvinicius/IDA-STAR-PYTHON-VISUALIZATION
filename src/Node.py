import util.Colors as Colors
import pygame as pg
import Node

pg.init()
FONT = pg.font.Font('freesansbold.ttf', 32)

class Node:
    g: float
    h: float
    selected = True
    moving = False

    def __init__(self, label: str, color, x, y, width = 50, height = 50):
        self.label = label
        self.color = color
        self.width = width
        self.height = height
        self.x = x - self.width // 2
        self.y = y - self.height // 2
        self.pos = (self.x, self.y)
        self.labelMesh = FONT.render(self.label, True, Colors.BLACK, Colors.WHITE)
        self.neighbors = []

    def addNeighbor(self, newNeighbor: Node):
        self.neighbors.append(newNeighbor)
        newNeighbor.neighbors.append(self)
    
    def getCenter(self):
        return (self.x + self.width // 2, self.y + self.height // 2)

    def draw(self, display: pg.Surface):
        pg.draw.rect(display, self.color, pg.Rect(self.x, self.y, self.width, self.height))
        labelRect = self.labelMesh.get_rect()
        display.blit(self.labelMesh, self.pos)
        if self.selected:
            pg.draw.rect(display, Colors.RED, pg.Rect(self.x, self.y, self.width, self.height), 2)

    def checkInput(self, pos) -> bool:
        if pos[0] in range(self.x , self.x + self.width) and pos[1] in range(self.y, self.y + self.height):
            self.selected = True
            return True

    def __str__(self) -> str:
        return self.label