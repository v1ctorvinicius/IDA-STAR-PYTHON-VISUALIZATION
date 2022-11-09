from Node import Node

def execute(nodes):
    f = open('util/nodesSave.txt', 'w')
    for node in nodes:
        f.write(node.label + ';' + str(node.pos))
        for neighbor in node.neighbors:
            f.write(';' + str(neighbor))
        f.write('\n')
    f.close()