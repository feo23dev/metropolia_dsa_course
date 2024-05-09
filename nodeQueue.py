class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"<ListNode: {self.data}>"


class Queue:
    def __init__(self):
        self._top = self._tail = None
        self._size = 0

    def enqueue(self, data):
        newNode = ListNode(data)

        if self._size == 0:

            self._top = self._tail = newNode

        else:

            current_node = self._top
            current_node.prev = newNode
            self._top = newNode
            newNode.next = current_node

        self._size += 1

    def dequeue(self):

        if not self._size:
            return None

        if self._size == 1:
            node_to_remove = self._tail
            self._tail = self._top = None
            self._size -= 1
            return node_to_remove

        node_to_remove = self._tail
        self._tail = node_to_remove.prev

        self._tail.next = None

        self._size -= 1
        return node_to_remove

    def __repr__(self):

        current_node = self._top
        values = ""
        while current_node:
            values += f", {current_node.data}"
            current_node = current_node.next

        plural = "" if self._size == 1 else "s"
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'


myQ = Queue()
myQ.enqueue("A")
myQ.enqueue("B")
myQ.enqueue("C")
print(myQ.dequeue())
print(myQ.dequeue())
print(myQ)
