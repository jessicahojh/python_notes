class Node(object):
    """Node in a tree"""

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []

    def add_to_tree(self, data, new_data):
        """Add node with new data to tree using DFS"""

        to_visit = [self] # assume not empty and no dupe

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                current.children.append(Node(new_data))

            to_visit.extend(current.children)

    def find_using_DFS(self, data):  # stack
        """return node object with this data."""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop()

            if current.data == data:
                return current

            to_visit.extend(current.children)

    def find_using_BFS(self, data):  # queue
        """return node object with this data."""

        to_visit = [self]

        while to_visit:
            current = to_visit.pop(0)

            if current.data == data:
                return current.data

            to_visit.extend(current.children)

food = Node('food', [Node('mexican'), Node('chinese'), Node('japanese')])
# mexican = Node('mexican', ['burritos', 'salsa', 'tacos'])
# chinese = Node('chinese', ['noodles', 'rice', 'dim sum'])
# japanese = Node('japanese', ['ramen', 'sushi', 'curry'])
food.add_to_tree('mexican', 'burritos')

print(food.find_using_BFS('burritos'))

    # Advantages:
    # Depth-first search on a binary tree generally requires less memory than breadth
    # -first.
    # Depth-first search can be easily implemented with recursion.

    # Disadvantages
    # A DFS doesn't necessarily find the shortest path to a node, while breadth-first 
    # search does.

    # Advantages:
    # A BFS will find the shortest path between the starting point and any other 
    # reachable node. A depth-first search will not necessarily find the shortest path.

    # Disadvantages
    # A BFS on a binary tree generally requires more memory than a DFS.