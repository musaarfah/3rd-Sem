class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, node, key):
# Basic BST insertion 
        if node is None:
            return TreeNode(key)
        if value < node.value:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, )
# Node itself is included in the height

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance(node)

# Means the left subtree is unbalanced
        if balance > 1:
            # Left Left Case
            if value < node.left.value:
                return self.rotate_right(node)
            # Left Right Case (left rotate the left child of node and then right rotate the node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
# Means the right subtree is Unbalanced
        if balance < -1:
            # Right Right Case
            if value > node.right.value:
                return self.rotate_left(node)
            # Right Left Case (Right rotate the right child and then left rotate the node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

   
    def delete(self, root, value):
        if root is None:
            return root
        
        if value < root.value:
            root.left = self.delete(root.left, value)
       
        elif value > root.value:
            root.right = self.delete(root.right, value)
        
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.get_min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)
        if root is None:
            return root
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1:
            if self.balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
        if balance < -1:
            if self.balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)
        return root

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

if __name__ == "__main__":
    avl_tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    for value in values:
        avl_tree.insert_value(value)

    print("Preorder traversal of the constructed AVL tree is:")
    avl_tree.preorder_traversal(avl_tree.root)
