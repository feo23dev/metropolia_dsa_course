class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f"<Node: {self.data}>"


class Stack:

    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):

        return self._top.data if self._top else None

    def push(self, data):

        new_node = Node(data)

        if self._size == 0:

            self._top = new_node
            self._top.next = None
            self._size += 1
            return

        else:

            current_node = self._top

            self._top = new_node
            new_node.next = current_node
            self._size += 1
            return

    def __repr__(self):
        if self._size == 0:
            return "<Stack (empty)>"

        current_node = self._top
        values = ""
        while current_node:
            values += f", {current_node.data}"
            current_node = current_node.next

        plural = "" if self._size == 1 else "s"
        return f'<Stack ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def pop(self):

        if self._size == 0:
            return None

        node_to_remove = self._top
        self._top = node_to_remove.next
        self._size -= 1
        return node_to_remove.data


ms = Stack()
ms.push("A")
ms.push("B")
ms.push("C")
ms.push("D")

ms.pop()

print(ms)
