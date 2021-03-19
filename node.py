class Node:
    def __init__(self, alphabets):
        self.alphabets= alphabets
        self.right = None
        self.left = None

    def setRight(self, newRight):
        self.right = newRight
    def setLeft(self, newLeft):
        self.left = newLeft
    def setValue(self, newValue):
        self.values = newValue
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def getAlphabets(self):
        return self.alphabets
