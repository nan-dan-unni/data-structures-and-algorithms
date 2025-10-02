class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data, root=None):
        new_node = Node(data)
        if root is None:
            if self.root is None:
                self.root = new_node
                return
            root = self.root

        if data < root.data:
            if root.left is None:
                root.left = new_node
            else:
                self.insert(data, root.left)
        else:
            if root.right is None:
                root.right = new_node
            else:
                self.insert(data, root.right)

    def preorder(self, node=None):
        if node is None:
            return []
        return [node.data] + self.preorder(node.left) + self.preorder(node.right)

    def inorder(self, node=None):
        if node is None:
            return []
        return self.preorder(node.left) + [node.data] + self.preorder(node.right)

    def postorder(self, node=None):
        if node is None:
            return []
        return self.preorder(node.left) + self.preorder(node.right) + [node.data]


if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(2)
    tree.insert(5)
    tree.insert(6)
    tree.insert(1)
    print(tree.preorder(tree.root))
    print(tree.inorder(tree.root))
    print(tree.postorder(tree.root))
