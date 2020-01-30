class linkedNode:

    def __init__(self, val = None):
        self.__val = val
        self.__nextNode = None

    def getVal(self):
        return self.__val

    def setVal(self, val):
        self.__val = val

    def setNextNode(self, node):
        self.__nextNode = node

    def getNextNode(self):
        return self.__nextNode


class mylinkedlist:

    def __init__(self, head = linkedNode()):
        self.__head = head

    def

    def addTail(self, linkedList):
        currentNode = self.__head

        while currentNode.getNextNode() is not None:
            currentNode = currentNode.getNextNode()

        currentNode.setNextNode(linkedList.getHead())

    
    