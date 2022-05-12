from typing import Optional


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# root:[TreeNode] means list of tree nodes
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.diameterOfBinaryTree(root.left) + self.diameterOfBinaryTree(root.right)
