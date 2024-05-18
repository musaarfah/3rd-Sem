import random
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
    
    def rotate(self, node, direction):
        if direction == "left":
            return self.rotate_left(node)
        elif direction == "right":
            return self.rotate_right(node)
        else:
            raise ValueError("Invalid rotation direction")

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
    
    def left_right_rotation(self, node):
        node.left = self.rotate_left(node.left)
        return self.rotate_right(node)

    def right_left_rotation(self, node):
        node.right = self.rotate_right(node.right)
        return self.rotate_left(node)

    def insert(self, node, key):
# Basic BST insertion 
        if node is None:
            return TreeNode(key)
        if key < node.value:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right,key )
# Node itself is included in the height

        node.height = 1 + max(self.height(node.left), self.height(node.right))

        balance = self.balance(node)

# Means the left subtree is unbalanced
        if balance > 1:
            # Left Left Case
            if key < node.left.value:
                return self.rotate_right(node)
            # Left Right Case (left rotate the left child of node and then right rotate the node)
            else:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)
# Means the right subtree is Unbalanced
        if balance < -1:
            # Right Right Case
            if key > node.right.value:
                return self.rotate_left(node)
            # Right Left Case (Right rotate the right child and then left rotate the node)
            else:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

        return node

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

   
    def inorder(self, p):
        if p.left:
            self.inorder(p.left)
        print(p.value, end=" ")
        if p.right:
            self.inorder(p.right)

    def inorder_traversal(self):
        if self.root:
            self.inorder(self.root)

    def getHeight(self):
        return self.height(self.root)
    

    # def calculateHeight(self, root):
    #     if root is None:
    #         return 0
    #     lh = self.calculateHeight(root.left)
    #     rh = self.calculateHeight(root.right)
    #     return max(lh, rh) + 1

tree = AVLTree()
for _ in range(500):
    val = random.randint(10,2000)
    tree.insert_value(val)
    print("Height:", tree.getHeight())
    print("\nIn Order:\t", end="")
    tree.inorder_traversal()