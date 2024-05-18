class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def set_value(self, value):
        self.value = value
    
    def set_left(self, left):
        self.left = left
    
    def set_right(self, right):
        self.right = right
    
    def get_value(self):
        return self.value
    
    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
class BinaryTree:
    def __init__(self):
        self.root = None
        self.count=0

# Insert Functions

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self.insert_recursive(self.root, value)
        self.count+=1
        

    def insert_leftchild(self, parent, child):
        parent.left = child
        self.count+=1

    def insert_rightchild(self, parent, child):
        parent.right = child
        self.count+=1


    def insert_recursive(self, node, value):
        if not node.left:
            node.left = TreeNode(value)
        elif not node.right:
            node.right = TreeNode(value)
        else:
            self.insert_recursive(node.left, value)

# Find Min

    def find_min(self, node):
        
        while node.left:
            node = node.left
        return node

# Delete Node

    def delete_element(self, element):
        self.root = self.delete_recursive(self.root, element)

    def delete_recursive(self, node, element):
        if node is None:
            return None
        if node.value == element:
            return None
        node.left = self.delete_recursive(node.left, element)
        node.right = self.delete_recursive(node.right, element)
        return node

    
# Display Function (post,In,Pre) 
    def display_pre_order(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.display_pre_order(node.left)
            self.display_pre_order(node.right)

    def display_in_order(self, node):
        if node is not None:
            self.display_in_order(node.left)
            print(node.value, end=" ")
            self.display_in_order(node.right)

    def display_post_order(self, node):
        if node is not None:
            self.display_post_order(node.left)
            self.display_post_order(node.right)
            print(node.value, end=" ")

# Counting Nodes

    def count_nodes(self):
            return self.count_nodes_recursive(self.root)

    def count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.count_nodes_recursive(node.left) + self.count_nodes_recursive(node.right)
    
    def min_value(self, node):
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.value
    
    def count_leaf_nodes(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self.count_leaf_nodes(node.left) + self.count_leaf_nodes(node.right)
    
# Non recursive (pre,post,In)
    
    def non_rec_pre_order(self):
        stack = []
        if self.root is None:
            return
        stack.append(self.root)
        while stack:
            node = stack.pop()
            print(node.value, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def non_rec_post_order(self):
        if self.root is None:
            return
        stack = []
        result = []
        stack.append(self.root)
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while result:
            print(result.pop(), end=" ")

    def non_rec_in_order(self):
        stack = []
        node = self.root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                print(node.value, end=" ")
                node = node.right

    def balancefactor(self, node):
        if node is None:
            return 0
        return self.height_of_tree_recursive(node.left) - self.height_of_tree_recursive(node.right)

    def display_ancestors(self, node_data):
        self.display_ancestors_recursive(self.root, node_data,[])

    def display_ancestors_recursive(self, node, node_data, ancestors):
        if node is None:
            return
        if node.value == node_data:
            print("Ancestors of", node_data, ":", ancestors)
            return
        self.display_ancestors_recursive(node.left, node_data, ancestors+[node.value])
        self.display_ancestors_recursive(node.right, node_data, ancestors+[node.value])

    def display_descendants(self, node_data):
        self.display_descendants_recursive(self.root, node_data)

    def display_descendants_recursive(self, node, node_data):
        if node is None:
            return
        if node.value == node_data:
            print("Descendants of", node_data, ":", end=" ")
            self.print_descendants(node.left)
            self.print_descendants(node.right)
            print()
        else:
            self.display_descendants_recursive(node.left, node_data)
            self.display_descendants_recursive(node.right, node_data)

    def print_descendants(self, node):
        if node is None:
            return
        print(node.value, end=" ")
        self.print_descendants(node.left)
        self.print_descendants(node.right)


    def height_of_tree(self):
        return self.height_of_tree_recursive(self.root)

    def height_of_tree_recursive(self, node):
        if node is None:
            return 0
        left_height = self.height_of_tree_recursive(node.left)
        right_height = self.height_of_tree_recursive(node.right)
        return max(left_height, right_height) + 1

    


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
# root.right.right.right = TreeNode(17)

bt1=BinaryTree()
# bt1.display_in_order(root)
# print()
# bt1.display_post_order(root)
# print()
# bt1.display_pre_order(root)

# print(bt1.balancefactor(root))





elements = [1, 2, 3, 4, 5, 6, 7]
bt = BinaryTree()
for element in elements:
    bt.insert(element)

# print(bt.height_of_tree())


# bt.non_rec_in_order()
# print()
# bt.non_rec_post_order()
# print()
# bt.non_rec_pre_order()






# bt.display_ancestors(5)
# print()

# bt.display_descendants(2)
# print()


# print(bt.find_min(bt.left))
    

    
