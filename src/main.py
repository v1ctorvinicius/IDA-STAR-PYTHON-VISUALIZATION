import sys
import pygame as pg
from pygame.locals import *

from Node import Node
from Edge import Edge
from Tree import Tree
from A_Star import A_Star
from Buttons import PlusButton
import util.Colors as Colors
import util.Save as Save
import util.Load as Load
from util.InputBox import InputBox

pg.init()


displaySize = DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600
display = pg.display.set_mode(displaySize)
pg.display.set_caption('IDA*')

FONT = pg.font.Font('freesansbold.ttf', 32)

INPUT_BOX = InputBox(DISPLAY_WIDTH // 2 + 50, int(DISPLAY_HEIGHT * 0.9), 140, 32)
PLUS_BUTTON = PlusButton(DISPLAY_WIDTH // 2, int(DISPLAY_HEIGHT * 0.9))

nodes = []
edges = []
Load.execute(nodes)

running = True
while running:
    keys = pg.key.get_pressed()

    if keys[pg.K_p]:
        pass

    if keys[pg.K_ESCAPE]:
        running = False

    if keys[pg.K_a]:
        for node in nodes:
            node.selected = False

    if keys[pg.K_d]:
        for node in nodes:
            if node.selected:
                nodes.remove(node)

    for event in pg.event.get():
        
        INPUT_BOX.handleEvent(event)
        
        if event.type == pg.QUIT:
            running = False

        # move nodes with mouse motion
        if event.type == pg.MOUSEMOTION:
            for node in nodes:
                if node.moving == True:
                    node.x += event.rel[0]
                    node.y += event.rel[1]
                    node.pos = (node.x, node.y)

        if event.type == pg.MOUSEBUTTONDOWN:
            mousePos = event.pos

            if event.button == pg.BUTTON_LEFT:
                resPlusButton = PLUS_BUTTON.checkInputDown(mousePos)

                # add node
                if(resPlusButton == True):
                    if INPUT_BOX.text != '':
                        newNode = Node(INPUT_BOX.text, Colors.WHITE, DISPLAY_WIDTH // 2 , DISPLAY_HEIGHT // 2)
                        nodes.append(newNode)
                    else:
                        print('coloque uma label para o nó')

                clickedAtLeastOneNode = 0
                for node in nodes:
                    res = node.checkInput(mousePos)
                    if res == True:
                        clickedAtLeastOneNode += 1
                if clickedAtLeastOneNode == 0:
                    for node in nodes:
                        node.selected = False

        # move nodes
        if event.type == pg.KEYDOWN:
            if event.unicode == 'm' or event.unicode == 'M':
                for node in nodes:
                    if node.selected == True:
                        node.moving = True

        # add edge
        if event.type == pg.KEYDOWN:
            if event.unicode == 'e':
                if INPUT_BOX.text != '':
                    edgeCost = int(INPUT_BOX.text)
                else:
                    print('coloque um peso para a aresta')

                counter = 0
                for node in nodes:
                    if node.selected == True:
                        counter += 1

                if counter == 2:
                    selectedNodes = []
                    for node in nodes:
                        if node.selected:
                            selectedNodes.append(node)
                    
                    selectedNodes[0].addNeighbor(selectedNodes[1])
                    newEdge = Edge(selectedNodes[0], selectedNodes[1], int(INPUT_BOX.text))
                    edges.append(newEdge)

        # stop moving nodes
        if event.type == pg.KEYUP:
            if event.unicode == 'm' or event.unicode == 'M':
                for node in nodes:
                    node.moving = False

        # save
        if event.type == pg.KEYUP:
            if event.unicode == 's':
                Save.execute(nodes)

    # loc = mx, my = pg.mouse.get_pos()

    display.fill(Colors.GREY)

    for edge in edges:
        edge.draw(display)

    for node in nodes:
        node.draw(display)

    rowCounter = 0
    spaceBetweenRows = 40
    for node in nodes:
        text = node.label + ': ' + str(node.pos)
        textMesh = FONT.render(text, True, Colors.GREEN, Colors.BLUE)
        textRect = textMesh.get_rect()
        textRect.y += rowCounter
        display.blit(textMesh, textRect)
        rowCounter += spaceBetweenRows 

    INPUT_BOX.draw(display)
    PLUS_BUTTON.draw(display)

    pg.display.update()

pg.quit()
sys.exit()