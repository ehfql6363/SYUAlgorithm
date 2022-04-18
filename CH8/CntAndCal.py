def countNode(n):
    if n is None:
        return 0
    else:
        return 1 + countNode(n.left) + countNode(n.right)

def countLeaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return countLeaf(n.left) + countLeaf(n.right)

def calcHeigth(n):
    if n is None:
        return 0
    hLeft = calcHeigth(n.left)
    hRight = calcHeigth(n.right)
    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1