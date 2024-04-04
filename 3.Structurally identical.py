#Given two generic trees, return true if they are structurally identical. Otherwise return false.
#Structural Identical
#If the two given trees are made of nodes with the same values and the nodes are arranged in the same way, then the trees are called identical.

from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def isIdentical(tree1, tree2):
    if tree1 is None or tree2 is None:
        return False

    if tree1.data != tree2.data:
        return False

    if len(tree1.children) != len(tree2.children):
        return False

    length = len(tree1.children)

    for i in range(length):
        if tree1.children[i].data != tree2.children[i].data:
            return False
        return isIdentical(tree1.children[i], tree2.children[i])

    return True



def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')
