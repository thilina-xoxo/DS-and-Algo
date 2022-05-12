# download recursion in programming
# depth first search, breadth first search
# How tree recusion happrn actually

class TreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


tree = TreeNode(10);  # root node
tree.left = TreeNode(20)
tree.right = TreeNode(5)
tree.left.left = TreeNode(12)
tree.left.right = TreeNode(14)

sol = Solution()
print(sol.maxDepth(tree))
