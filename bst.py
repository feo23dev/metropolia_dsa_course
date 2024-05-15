class Node:
    def __init__(self, data, parent_node=None, left_child=None, right_child=None):
        self.data = data
        self._parent_node = parent_node
        self._left_child = left_child
        self._right_child = right_child


class BinarySearchTree:
    def __init__(self):
        self._root_node = None

    def insert(self, data):
        # To find where to insert this new Node
        # it will start at the root node, compare the new value
        # move right or left until there is no more Node
        current_node = self._root_node

        parent_node = None

        while current_node:
            parent_node = current_node
            if data <= current_node.data:
                current_node = current_node._left_child
            else:
                current_node = current_node._right_child
            return

        new_node = Node(data, parent_node=parent_node)

        if parent_node is None:
            # Tree is empty ,make new node the root node
            self._root_node = new_node
        elif new_node.data < parent_node.data:
            parent_node._left_child = new_node
        else:
            parent_node._right_child = new_node
        return

    def _find(self, data):

        current_node = self._root_node

        while current_node:

            if data < current_node.data:
                current_node = current_node._left_child

            elif data > current_node.data:
                current_node = current_node._right_child

            else:
                return current_node
        return None

    def find_minimum(self):
        current_node = self._root_node
        parent = None
        while current_node:
            parent = current_node
            current_node = current_node._left_child
        return parent

    def find_maximum(self):
        """
        Returns the maximum value of the tree
        """
        current_node = self._root_node
        parent = None
        while current_node:
            parent = current_node
            current_node = current_node._right_child
        return parent


tree = BinarySearchTree()
print(tree.insert(10))
