class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None

chars = ['A','B','C','D','E','F']
nodes = [ Node(x) for x in chars]
nodes[0].left = nodes[1];
nodes[0].right = nodes[2];

nodes[1].left = nodes[3];

nodes[2].right = nodes[5];
nodes[5].left = nodes[4];

def dispPre(node):
    if(node == None):
        return
    print(node.value, end= ' ')
    dispPre(node.left)
    dispPre(node.right)
dispPre(nodes[0])
print()

def dispMid(node):
    if(node == None):
        return
    dispMid(node.left)
    print(node.value, end= ' ')
    dispMid(node.right)
dispMid(nodes[0])
print()

def dispLast(node):
    if(node == None):
        return
    dispLast(node.left)
    dispLast(node.right)
    print(node.value, end= ' ')
dispLast(nodes[0])
print()


def getHeight(node):
    if(node == None):
        return 0
    return max(getHeight(node.left), getHeight(node.right)) + 1

print('Height:', getHeight(nodes[0]));