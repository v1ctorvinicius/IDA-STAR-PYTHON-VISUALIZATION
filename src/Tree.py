from Node import Node
import Tree

class Tree:
    def __init__(self, root: Node = None):
        self.root = root

        if(root == None):
            self.root = self.__montarArvore()

    
    def printTree(self, root, level = 0):
        print("    " * level, "|->", root)
        for child in root.children:
            self.printTree(child, level + 1)

    def __montarArvore(self) -> Node:
        a = Node("a", 0)
        b = Node("b", 2)
        c = Node("c", 3)
        d = Node("d", 1)
        e = Node("e", 1)
        f = Node("f", 6)
        g = Node("g", 2)
        h = Node("h", 4)
        i = Node("i", 4)
        j = Node("j", 4)
        k = Node("k", 3)
        l = Node("l", 2)
        m = Node("m", 5)
        n = Node("n", 4)
        o = Node("o", 1)
        p = Node("p", 2)
        q = Node("q", 3)
        r = Node("r", 3)
        s = Node("s", 1)
        t = Node("t", 2)
        u = Node("u", 4)
        v = Node("v", 3)

        a.addChild(b, 4)
        a.addChild(c, 3)
        a.addChild(d, 1)

        b.addChild(e, 2)

        c.addChild(f, 1)
        c.addChild(g, 2)

        d.addChild(h, 2)

        e.addChild(i, 4)

        f.addChild(j, 3)

        g.addChild(k, 3)
        g.addChild(l, 2)
        g.addChild(m, 5)

        h.addChild(n, 3)
        h.addChild(o, 5)

        i.addChild(p, 6)
        i.addChild(q, 2)

        l.addChild(r, 2)

        n.addChild(s, 1)
        n.addChild(t, 2)
        n.addChild(u, 5)

        o.addChild(v, 2)

        return a
        