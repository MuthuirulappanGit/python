class Node:
    def __init__(self, title):
        self.title = title
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, title):
        new_node = Node(title)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if title < current.title:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.title)
            self.inorder(node.right)



tree = BinarySearchTree()

n = int(input("Enter number of books: "))

for i in range(n):
    title = input("Enter book title: ")
    tree.insert(title)

print("\nBook titles in alphabetical order:")
tree.inorder(tree.root)
