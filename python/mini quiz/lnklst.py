class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.is_frozen = False

    def add(self, value):
        if self.is_frozen:
            print("Cannot add new nodes. The list is frozen.")
            return
        
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def freeze(self):
        self.is_frozen = True

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

bitcoin = LinkedList()

for char in "Bitcoin":
    bitcoin.add(char)

bitcoin.freeze()

bitcoin.display()

bitcoin.add('X')