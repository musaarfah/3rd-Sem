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
    
    def delete_node(self, value):
        self.root = self._delete_node_recursive(self.root, value)

    def _find_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def _delete_node_recursive(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self._delete_node_recursive(root.left, value)
        elif value > root.value:
            root.right = self._delete_node_recursive(root.right, value)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor (smallest
            # in the right subtree) or predecessor (largest in the left subtree)
            temp = self._find_min_value_node(root.right)

            # Copy the inorder successor's content to this node
            root.value = temp.value

            # Delete the inorder successor
            root.right = self._delete_node_recursive(root.right, temp.value)

        return root

    
    def print_tree(self):
        self._print_inorder(self.root)

    def _print_inorder(self, node):
        if node is not None:
            self._print_inorder(node.left)
            print(node.value,end=' ')
            self._print_inorder(node.right)
    

bst = BinarySearchTree()
bst.insert(5)
bst.insert(7)
bst.insert(-2)
bst.insert(43)
bst.insert(9)
bst.insert(15)
bst.print_tree()

                



