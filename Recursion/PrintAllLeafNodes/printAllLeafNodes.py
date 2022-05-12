class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def printAllLeafNodes(self, root: [TreeNode]):
        if (not root.left) and (not root.right):  # there are no children in the leaf node
            print(root.value)
            return
        if root.left:
            self.printAllLeafNodes(root.left)
        if root.right:
            self.printAllLeafNodes(root.right)
