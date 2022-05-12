from typing import Optional


class TreeNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

# Optional keyword in python
class Solution:
    def invertBinaryTree(self, root:Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None


        temp = root.left
        root.left = root.right
        root.left = temp
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root

