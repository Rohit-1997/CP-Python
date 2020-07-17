class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        new_node = Node(new_val)
        if not self.root:
            self.root = new_node

        current = self.root

        while True:
            if new_val <= current.value:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
                    continue
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
        

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        if not self.root:
            return False
        if self.root.value == find_val:
            return True

        current = self.root
        while current is not None:
            if current.value == find_val:
                return True
            if current.value < find_val:
                current = current.left
            else:
                current = current.right

