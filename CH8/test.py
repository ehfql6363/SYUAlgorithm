from CH8.CntAndCal import countNode, countLeaf, calcHeigth
from CH8.TNode import TNode
from CH8.Order import preorder, inorder, postorder, levelorder

d = TNode('D', None, None)
e = TNode('E', None, None)
f = TNode('F', None, None)
b = TNode('B', d, e)
c = TNode('C', f, None)
root = TNode('A', b, c)

print("전위 : ", end=' ')
preorder(root)
print("\n중위 : ", end=' ')
inorder(root)
print("\n후위 : ", end=' ')
postorder(root)
print("\n레벨 : ", end=' ')
levelorder(root)
print()

print(f"노드의 개수 : {countNode(root)}개")
print(f"단말 노드의 개수 : {countLeaf(root)}개")
print(f"트리의 높이 : {calcHeigth(root)}")