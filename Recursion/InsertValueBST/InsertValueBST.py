from typing import Optional


class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def addValuetoBST(self, head: Optional[TreeNode], value: int):

        # base case
        if not head:
            head = TreeNode(value)
            return head
        if head.value < value:
            head.right = self.addValuetoBST(head.right, value) # we have to create the connection with new node that is why equal is there
        else:
            head.left = self.addValuetoBST(head.right, value)

        return head
