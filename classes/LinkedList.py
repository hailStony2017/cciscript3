from random import randint


class Node(object):
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


    def __str__(self):
        return str(self.data)


class LinkedList(object):
    def __init__(self, data):
        self.head = None
        self.tail = None
        if data is not None:
            for d in data:
                self.add_to_end(d)


    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __str__(self):
        data = [str(x.data) for x in self]
        return " -> ".join(data)

    def __len__(self):
        length = 0
        node = self.head
        while node:
            length += 1
            node = node.next
        return length

    def add_to_end(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = self.tail.next

        return self.head

    def add_to_beginning(self, data):
        if self.head is None:
            self.tail = self.head = Node(data)
        else:
            self.head = Node(data, self.head)

        return self.head


class DoublyLinkedList(LinkedList):
    def __init__(self):
        super(DoublyLinkedList, self).__init__()

    def add_to_end(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            self.head.next = new_node
            new_node.prev = self.head

        return self.head

    def add_to_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self.head = Node(data, self.head)
            self.head.next.prev = self.head

        return self.head