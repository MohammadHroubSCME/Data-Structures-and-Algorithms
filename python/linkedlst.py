class linkedlist:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def add(self, e):
        newnode = Node(e)
        newnode.next = self.__head
        self.__head = newnode
        self.__size += 1

        if self.__tail == None:
            self.__tail = self.__head


class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

    def insert(self, index, e):
        if index == 0:
            self.addfirst(e)
        elif index >= self.__size:
            self.addlast(e)
        else:
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1