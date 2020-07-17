class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)


    def search_helper(self,node,value):
        if node is None:
            return False
        if node.value == value:
            return True
        left_result = self.search_helper(node.left,value)
        if left_result:
            return True
        right_result = self.search_helper(node.right, value)
        return right_result
        

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        if not self.root:
            return False
        return self.search_helper(self.root,find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        pass

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        pass

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.search(7))