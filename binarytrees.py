class node:
    def __init__(self, val):
        self.__left = None
        self.__right = None
        self.__val = val

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def getVal(self):
        return self.__val

# left, root, right
def printInorder(root):

    # checking to see if root exists
    if root:
        printInorder(root.getLeft())
        print(root.getVal())
        printInorder(root.getRight())

# root, left, right
def printPreorder(root):

    if root:
        print(root.getVal())
        printPreorder(root.getLeft())
        printPreorder(root.getRight())

# left, right, root
def printPostorder(root):

    if root:
        printPostorder(root.getLeft())
        printPostorder(root.getRight())
        print(root.getVal())
    