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
        # if not self.root:
        #     self.root = new_node

        # current = self.root

        # while True:
        #     if new_val <= current.value:
        #         if current.left is None:
        #             current.left = new_node
        #             break
        #         else:
        #             current = current.left
        #             continue
        #     else:
        #         if current.right is None:
        #             current.right = new_node
        #             break
        #         else:
        #             current = current.right
        temproot = self.root
        while temproot != None:
            print(temproot.value)
            if new_val > temproot.value:
                if temproot.right is None:
                    temproot.right = new_node
                    break
                temproot = temproot.right
            else:
                if temproot.left is None:
                    temproot.left = new_node
                    break
                temproot = temproot.left
        # temproot = new_node
        

    def printSelf(self):
        # Your code goes here
        if self.root is None:
            return
        queue = [self.root]

        while queue != []:
            current = queue.pop(0)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
    def search(self, find_val):
        if not find_val or type(find_val) != int:
            return False
        if not self.root:
            return False
        if self.root.value == find_val:
            return True

        current = self.root
        while current is not None:
            print(current.value)
            if current.value == find_val:
                print("found case")
                return True
            if find_val < current.value:
                current = current.left
            else:
                current = current.right
        return False


tree = BST(4)
# print(tree.search(4))
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
tree.printSelf()
# print(tree.search("6"))