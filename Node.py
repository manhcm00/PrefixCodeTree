class Node:
    right,left,data = None,None, ''

    def __init__(self,key):
        self.right = None
        self.left = None
        self.data = key

    def isLeave(self):
        return self.right is None and self.left is None