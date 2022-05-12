class Node(object):  # what is mean by this object parameter
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self, root):  # when tree is creating this constructor involves with the process
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root,"")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root,"")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root,"")

    def preorder_print(self, start, traversal):
        """ Root -> Left -> Right """

        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right, traversal)

        return traversal

    def inorder_print(self, start, traverasal):
        """ Left -> Root -> Right """
        if start:
            traverasal = self.inorder_print(start.left,traverasal)
            traverasal += (str(start.value)+ "-")
            traverasal = self.inorder_print(start.right,traverasal)

        return traverasal

    def postorder_print(self, start, traversal):
        """ Left -> Right -> Root """

        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")

        return traversal





# lets build a tree

tree = BinaryTree(1) # valueo of the root node

tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

# tree traversal
# can be traversed in depth-first or breadth-first
# depth first order -> In order, pre-order, post order

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))

