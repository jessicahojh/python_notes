# A Binary Tree Node can have two children

class BinaryTreeNode(object):

    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right

    def insert_sorted(self, new_data):

        current = self

        prev_head = None

        while current:

            prev_head = current
        
            if new_data < current.data: 
                current = current.left

            elif new_data > current.data: 
                current = current.right

        if new_data < prev_head.data:
            prev_head.left = BinaryTreeNode(new_data)

        elif new_data > prev_head.data:
            prev_head.right = BinaryTreeNode(new_data)


    def print_tree_pre_order(self): 

        current = self

        print(current.data)

        if current.left:
            current.left.print_tree_pre_order()

        if current.right:
            current.right.print_tree_pre_order()

    def print_tree_in_order(self):

        current = self

        if current.left:
            current.left.print_tree_in_order()

        print(current.data)

        if current.right:
            current.right.print_tree_in_order()

    def print_tree_post_order(self): 

        current = self

        if current.left:
            current.left.print_tree_post_order()

        if current.right:
            current.right.print_tree_post_order()

        print(current.data)

    def find(self, sought):
        """return node with this data"""

        current = self

        while current:

            if current.data == sought:
                return current.data

            elif sought < current.data:
                current = current.left

            elif sought > current.data:
                current = current.right


tree = BinaryTreeNode(10)
tree.insert_sorted(4)
tree.insert_sorted(20)
tree.insert_sorted(6)
tree.insert_sorted(25)
tree.insert_sorted(1)
tree.insert_sorted(3)

# tree = BinaryTreeNode(1)
# tree.left = BinaryTreeNode(2)
# tree.right = BinaryTreeNode(3)
# tree.left.left = BinaryTreeNode(4)
# tree.left.right = BinaryTreeNode(5)
# tree.right.left = BinaryTreeNode(6)
# tree.right.right = BinaryTreeNode(7)

tree.print_tree_pre_order() 
print("")
tree.print_tree_in_order() 
print("")
tree.print_tree_post_order() 

print(tree.find(6))