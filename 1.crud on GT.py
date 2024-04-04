import queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

#we will print in preorder here, but this does not tell us exactly whose child is whom
def printTree(root):
    #this is a edge case but not a base case
    if root == None:
        return
    print(root.data)
    for child in root.children:
        printTree(child)
        
#print the tree so that structure will be clearly seen
def printTreeDetailed(root):
    if root == None:
        return
    
    print(root.data, ':', end='')
    for child in root.children:
        print(child.data, ',', end='')
    print()
    for child in root.children:
        printTreeDetailed(child)

def takeTreeInput():
    print('enter root data')
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)

    print('Enter number of children for', rootData)
    childrenCount = int(input())
    for i in range(childrenCount):
        child = takeTreeInput()
        root.children.append(child)
    return root

def numNodes(root):
    if root == None:
        return 0
    count = 1
    for child in root.children:
        count = count + numNodes(child)
    return count

def sumOfAllNodes(root) :
    if root is None:
        return 0
    count = root.data
    for child in root.children:
        count = count + sumOfAllNodes(child)
    return count

def maxDataNode(tree):
    if tree is None:
        return
    maximum = tree.data
    for child in tree.children:
        maximum = max(maximum, maxDataNode(child))
    return maximum

def height(tree):
    if tree is None:
        return 0
    count = 0
    for child in tree.children:
        childHeight = height(child)
        count = max(childHeight, count)
    count += 1
    return count

#level wise input
def takeLevelWise():
    q = queue.Queue()
    print('Enter root')
    rootData = int(input())
    if rootData == -1:
        return None

    root = TreeNode(rootData)
    q.put(root)
    while (not(q.empty())):
        current_node =  q.get()
        print('Enter num of children for ', current_node.data)
        numChildren = int(input())
        for i in range(numChildren):
            print('Enter next child for ', current_node.data)
            childData = int(input())
            child = TreeNode(childData)
            current_node.children.append(child)
            q.put(child)
    return root

def printLevelWiseTree(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():

        while not inputQ.empty():

            curr = inputQ.get()
            print(curr.data, end=':')
            for child in curr.children:
                outputQ.put(child)
                if child == curr.children[-1]:
                    print(child.data, end='')
                else:
                    print(child.data, end=',')

            print()

        inputQ, outputQ = outputQ, inputQ

def containsX(tree, x):
    if tree is None:
        return False

    if tree.data == x:
        return True

    for child in tree.children:
        if containsX(child, x):
            return True

    return False

def leafNodeCount(tree):
    if tree is None:
        return 0
    count = 0
    for child in tree.children:
        count = count + leafNodeCount(child)
    if len(tree.children) == 0:
        count += 1
    return count

root = takeTreeInput()
printTreeDetailed(root)
