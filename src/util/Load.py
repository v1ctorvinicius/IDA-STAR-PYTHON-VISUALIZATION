from Node import Node
import util.Colors as Colors

def execute(nodes):
    f = open('util/save.txt', 'r')
    line = f.readline()
    cnt = 1
    while line:
        line = line.strip('\n')
        data = line.split(';')

        print(data)
        label = data[0]
        color = Colors.WHITE
        x = data[1][0] # ERROR HERE
        y = data[1][1]
        newNode = Node(label, color, int(x), int(y))

        nodes.append(newNode)    

        line = f.readline()
        cnt += 1
    f.close()

