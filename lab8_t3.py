import random


class BST:
    class BTNode:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right
    def __init__(self):
        self.root = None

    def add(self, d, t):
        if t is None:
            return self.BTNode(d)
        if t.data > d:
            t.left = self.add(d, t.left)
        elif t.data < d:
            t.right = self.add(d, t.right)
        return t

    def add_node(self, d):
        self.root = self.add(d, self.root)

    def inorder(self, t):
        if t is not None:
            self.inorder(t.left)
            print(t.data, end=' ')
            self.inorder(t.right)

    def inorder_traversal(self):
        self.inorder(self.root)
        print()

    def preorder(self, t):
        if t is not None:
            print(t.data, end=' ')
            self.preorder(t.left)
            self.preorder(t.right)

    def preorder_traversal(self):
        self.preorder(self.root)
        print()

    def count_nodes(self, t): 
        if t is None:
            return 0
        return 1 + self.count_nodes(t.left) + self.count_nodes(t.right)
    
    def inorder_array(self, t, array, index):
        if t is not None:
            index = self.inorder_array(t.left, array, index)
            array[index] = t.data
            index += 1
            index = self.inorder_array(t.right, array, index)
        return array
    
    def add_binary_search(self, array, start, end):
        if start <= end:
            mid = (start + end) // 2
            self.add_node(array[mid])
            self.add_binary_search(array, start, mid - 1)
            self.add_binary_search(array, mid + 1, end)


    def check_and_balance_tree(self, count_nodes):
        array = [None] * count_nodes
        self.inorder_array(self.root, array, 0)
        self.root = None
        self.add_binary_search(array, 0, len(array) - 1)

    def check_and_balance(self):
        left_count = self.count_nodes(self.root.left)
        right_count = self.count_nodes(self.root.right)
        diff = left_count - right_count
        if abs(diff) > 1:
            self.check_and_balance_tree(left_count + right_count + 1)

    def remove_nodes(self, t):
        if t is None:
            return
        self.remove_nodes(t.left)
        self.remove_nodes(t.right)
        del t

    def __del__(self):
        self.remove_nodes(self.root)


if __name__ == "__main__":
    # tree = BST()
    # for _ in range(10):
    #     tree.add_node(random.randint(1, 10))
    # tree.preorder_traversal()
    # tree.inorder_traversal()
    # tree.preorder_traversal()
    # tree.inorder_traversal()

    # tree.check_and_balance()
    # bst = BST()

    # sorted_array = [2, 3, 5, 7, 8, 9]

    # bst.add_binary_search(sorted_array, 0, len(sorted_array) - 1)
    # bst.inorder_traversal()
    # bst.preorder_traversal()

    # bst = BST()
    # bst.add_node(6)
    # bst.add_node(3)
    # bst.add_node(1)
    # bst.add_node(19)
    # bst.add_node(9)
    # bst.add_node(4)
    # bst.add_node(11)

    # array = [None] * bst.count_nodes(bst.root)

    # bst.inorder_array(bst.root, array, 0)

    # print(array)

    bst = BST()
    bst.add_node(6)
    bst.add_node(3)
    bst.add_node(1)
    bst.add_node(19)
    bst.add_node(9)
    bst.add_node(4)
    bst.add_node(11)

# calculate the balnce factor
    print("Balance before balancing:", abs(bst.count_nodes(bst.root.left) - bst.count_nodes(bst.root.right)) <= 1)

    bst.check_and_balance_tree(bst.count_nodes(bst.root))

    print("Balance after balancing:", abs(bst.count_nodes(bst.root.left) - bst.count_nodes(bst.root.right)) <= 1)