from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []


def nextLargest(tree, n, just=treeNode(None)):

    if tree is None:
        return
    if tree.data > n:
        just = tree
    for child in tree.children:
        justChild = nextLargest(child, n, just)
        if (just.data is not None and justChild.data is not None and just.data > justChild.data) or just.data is None:
            just = justChild

    return just





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
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
if nextLargest(tree, n).data is not None:
    print(nextLargest(tree, n).data)
