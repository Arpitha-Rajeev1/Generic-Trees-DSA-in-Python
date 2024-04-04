from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans


def helper(root, resNode, maxsum):
    if root is None:
        return
    currsum = root.data
    count = len(root.children)

    for i in range(0, count):
        currsum += root.children[i].data
        resNode, maxsum = helper(root.children[i], resNode, maxsum)

    if currsum > maxsum:
        resNode = root
        maxsum = currsum

    return resNode, maxsum


def maxSumNode(root):
    resNode, maxsum = treeNode(None), 0
    resNode, maxsum = helper(root, resNode, maxsum)

    return resNode


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
tree = createLevelWiseTree(arr)
temp = maxSumNode(tree)
print(temp.data)
