class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root

        if current is None:
            current.value = new_val
            return
        while current:
            if current.value < new_val:
                if current.right is None:
                    current.right = Node(new_val)
                    return
                current= current.right
            else:
                if current.left is None:
                    current.left = Node(new_val)
                    return
                current = current.left

    def search(self, find_val):
        current = self.root
        if current.value == find_val:
            return True
        while current:
            if current.value < find_val:
                if current.right:
                    if current.right.value == find_val:
                        return True
                current = current.right
            else:
                if current.left:
                    if current.left.value == find_val:
                        return True
                current = current.left
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))