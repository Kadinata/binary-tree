#!/usr/bin/python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if (value <= self.value):
            if (self.left is None):
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if (self.right is None):
                self.right = Node(value)
            else:
                self.right.insert(value)