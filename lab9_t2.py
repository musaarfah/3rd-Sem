class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def construct_from_traversals(self, in_order, pre_order):
        if not in_order or not pre_order or len(in_order) != len(pre_order):
            return None

        def build_tree(in_start, in_end, pre_start):
            if in_start > in_end:
                return None, pre_start

            root_data = pre_order[pre_start]
            root = TreeNode(root_data)

            in_index = in_order.index(root_data)
            pre_start += 1

            root.left, pre_start = build_tree(in_start, in_index - 1, pre_start)
            root.right, pre_start = build_tree(in_index + 1, in_end, pre_start)

            return root, pre_start

        self.root, _ = build_tree(0, len(in_order) - 1, 0)
        return self.root

    def display_in_order(self, node):
        if node:
            self.display_in_order(node.left)
            print(node.data, end=' ')
            self.display_in_order(node.right)

    def display_post_order(self, node):
        if node:
            self.display_post_order(node.left)
            self.display_post_order(node.right)
            print(node.data, end=' ')

bst = BinarySearchTree()
in_order = ['D', 'B', 'E', 'A', 'F', 'C']
pre_order = ['A', 'B', 'D', 'E', 'C', 'F']
bst.root = bst.construct_from_traversals(in_order, pre_order)
print("In-order traversal of constructed BST:")
bst.display_in_order(bst.root)
print("\nPost-order traversal of constructed BST:")
bst.display_post_order(bst.root)

# Driver code for example 2
bst2 = BinarySearchTree()
in_order = [5, 10, 15, 25, 27, 30, 35, 40, 45, 50, 52, 55, 60, 65, 70, 75, 80, 85, 90, 100]
pre_order = [50, 25, 10, 5, 15, 40, 30, 27, 35, 45, 75, 60, 55, 52, 65, 70, 90, 80, 85, 100]
bst2.root = bst2.construct_from_traversals(in_order, pre_order)
print("\nIn-order traversal of constructed BST:")
bst2.display_in_order(bst2.root)
print("\nPost-order traversal of constructed BST:")
bst2.display_post_order(bst2.root)