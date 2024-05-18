class TreeNode:
    def __init__(self,value=0):
        self.parent=None
        self.left=None
        self.right=None
        self.value=value

class BinarySearchTree:
    def __init__(self):
        self.root=None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.insert_recursive(self.root, value)

    def insert_recursive(self,node,value):
        if value < node.value:
            if node.left is None:
                node.left=TreeNode(value)
            else:
                self.insert_recursive(node.left,value)

        elif value> node.value:
            if node.right is None:
                node.right=TreeNode(value)
            else:
                self.insert_recursive(node.right,value)

        else:
            pass
# Search element

    def search(self,value):
        current = self.root
        while current:
            if current.value == value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

# Delete Node

    def delete_node(self, value):
        self.root = self._delete_node_recursive(self.root, value)

    def find_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete_node_recursive(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.delete_node_recursive(root.left, value)
        elif value > root.value:
            root.right = self.delete_node_recursive(root.right, value)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            
            temp = self.find_min_value_node(root.right)

            root.value = temp.value

            root.right = self.delete_node_recursive(root.right, temp.value)

        return root
                    

# Pre Order display 
    def display_preorder(self):
        self.display_preorder_recursive(self.root)
        print()

    def display_preorder_recursive(self, node):
        if node:
            print(node.value, end=" ")
            self.display_preorder_recursive(node.left)
            self.display_preorder_recursive(node.right)

# Inorder Display
    def display_inorder(self):
        self.display_inorder_recursive(self.root)
        print()

    def display_inorder_recursive(self, node):
        if node:
            self.display_inorder_recursive(node.left)
            print(node.value, end=" ")
            self.display_inorder_recursive(node.right)
# Post Order Display
    def display_postorder(self):
        self.display_postorder_recursive(self.root)
        print()

    def display_postorder_recursive(self, node):
        if node:
            self.display_postorder_recursive(node.left)
            self.display_postorder_recursive(node.right)
            print(node.value, end=" ")
    def total_elements(self):
        return self._count_elements_recursive(self.root)

    def _count_elements_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_elements_recursive(node.left) + self._count_elements_recursive(node.right)



elements = [1, 2, 3, 4, 5, 6, 7]
bst = BinarySearchTree()
for element in elements:
    bst.insert(element)

# bst.display_inorder()
# bst.display_postorder()
# bst.display_preorder()
                
# print(bst.total_elements())


