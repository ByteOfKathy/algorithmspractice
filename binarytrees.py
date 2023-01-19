class node:
    def __init__(self, val):
        self.__left = None
        self.__right = None
        self.__val = val

    # getters

    def getRight(self):
        return self.__right

    def getLeft(self):
        return self.__left

    def getVal(self):
        return self.__val

    # setters

    def setRight(self, val):
        self.__right = val

    def setLeft(self, val):
        self.__left = val

    def setVal(self, val):
        self.__val = val

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

def printLevelOrder(root):
    if root:
        # queue
        q = []
        q.append(root)

        while q:
            height = len(q)
            while height > 0:
                temp = q.pop(0)
                print(temp.getVal(), end = ' ')
                if temp.getLeft():
                    q.append(temp.getLeft())
                if temp.getRight():
                    q.append(temp.getRight())
                height -= 1
            print()

# main
root = node(1)
root.setLeft(node(2))
root.setRight(node(3))
root.getLeft().setLeft(node(4))
root.getLeft().setRight(node(5))
root.getRight().setRight(node(6))
 
printLevelOrder(root)