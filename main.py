#!/usr/bin/python
from binarytree import Node
import sys

TREE_1 = Node(4)
TREE_1.insert(2)
TREE_1.insert(5)
TREE_1.insert(1)
TREE_1.insert(3)

def build123():
    root = Node(2)
    root.insert(1)
    root.insert(3)
    return root

def size(root):
    if (root is None):
        return 0
    return 1 + size(root.left) + size(root.right)

def maxDepth(root):
    if (root is None):
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

def minValue(root):
    if (root is None):
        return 0
    elif ((root.left is None) and (root.right is None)):
        return(root.value)
    elif (root.left is None):
        return min(root.value, minValue(root.right))
    elif(root.right is None):
        return min(root.value, minValue(root.left))
    return min(root.value, minValue(root.left), minValue(root.right))

def maxValue(root):
    if (root is None):
        return 0
    elif ((root.left is None) and (root.right is None)):
        return(root.value)
    elif (root.left is None):
        return max(root.value, maxValue(root.right))
    elif(root.right is None):
        return max(root.value, maxValue(root.left))
    return max(root.value, maxValue(root.left), maxValue(root.right))

def printTree(root):
    if (root is None):
        return
    printTree(root.left)
    print(root.value)
    printTree(root.right)

def printPostorder(root):
    if (root is None):
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.value)

def hasPathSum(root, sum):
    if (root is None):
        return False
    sum = (sum - root.value)
    if ((not root.left) and (not root.right)):
        return (sum == 0)
    return (hasPathSum(root.left, sum) or hasPathSum(root.right, sum))

def getRowValue(root, row_index, arr=[], start_idx=0, tree_size=None):
    if (root is None): return
    if (tree_size is None):
        tree_size = (2 ** maxDepth(root)) - 1
    subtree_size = (tree_size - 1) / 2
    current_idx = subtree_size + start_idx
    if (row_index == 0):
        arr[current_idx] = str(root.value)
    else:
        row_index -= 1
        getRowValue(root.left, row_index, arr, start_idx, subtree_size)
        getRowValue(root.right, row_index, arr, current_idx+1, subtree_size)

def printPaths(root):
    if (root is None): return
    tree_size = (2 ** maxDepth(root)) - 1
    for row in range(maxDepth(root)):
        tree_array = [' '] * tree_size
        getRowValue(root, row, tree_array)
        print(''.join(tree_array))

def mirror(root):
    if (root is None): return
    node = Node(root.value)
    node.right = mirror(root.left)
    node.left = mirror(root.right)
    return node

def doubleTree(root):
    if (root is None): return
    node = Node(root.value)
    node.insert(root.value)
    node.left.left = doubleTree(root.left)
    node.right = doubleTree(root.right)
    return node

def sameTree(tree1, tree2):
    if (tree1 is None):
        return (tree2 is None)
    if (tree2 is None):
        return (tree1 is None)
    return (
        (tree1.value == tree2.value)
        and sameTree(tree1.left, tree2.left)
        and sameTree(tree1.right, tree2.right)
    )

def countTrees(numKeys):
    if (numKeys <= 1): return 1
    sum = 0
    for i in range(numKeys):
        sum += countTrees(i) * countTrees(numKeys - 1 - i)
    return sum

def isBST1(root):    
    if (root is None): return True
    if ((root.left) and (maxValue(root.left) > root.value)):
        return False
    if ((root.right) and (minValue(root.right) < root.value)):
        return False
    return (isBST1(root.left) and isBST1(root.right))

def isBSTRecur(root, minVal, maxVal):
    if (root is None): return True
    if ((root.value < minVal) or (root.value > maxVal)):
        return False
    return (isBSTRecur(root.left, minVal, root.value) and isBSTRecur(root.right, root.value, maxVal))

def main():
    root = build123()
    print(size(root))
    print(maxDepth(root))
    print(minValue(root))
    printTree(root)
    printPaths(TREE_1)
    printPaths(mirror(TREE_1))
    printPaths(doubleTree(root))
    printPaths(doubleTree(TREE_1))
    print(sameTree(TREE_1, TREE_1))
    print(sameTree(TREE_1, root))

    for i in range(6):
        print(i, countTrees(i))

    print(minValue(mirror(TREE_1)))
    print(isBST1(doubleTree(TREE_1)))
    print(isBST1(mirror(doubleTree(TREE_1))))
    print(isBSTRecur(TREE_1, -100, 100))
    print(isBSTRecur(mirror(TREE_1), -100, 100))

if __name__ == "__main__":
    main()