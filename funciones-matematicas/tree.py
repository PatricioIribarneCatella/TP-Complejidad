class Node:

    def __init__(self, val, level, n):

        self.val = val
        self.n = n
        self.children = []
        
        if level > 0:
            for i in range(n):
                if i != self.val:
                    self.children.append(Node(i, level - 1, n))

    def hasChildren(self):
        return len(self.children) > 0

    def getValue(self):
        return self.val

    def getChildren(self):
        return self.children


def visit(r, node, n):

    r.append(node.getValue())

    if node.hasChildren():
        for e in node.getChildren():
            visit(r, e, n)
        r.pop()
    else:
        s = set(r)
        if len(s) == n:
            print(r)
        r.pop()
        return

def perm(data):

    n = len(data)

    t = [Node(i, n - 1, n) for i in range(n)]

    r = []

    for node in t:
        visit(r, node, n)

def main():

    perm([1,2,3])

if __name__ == "__main__":

    main()

