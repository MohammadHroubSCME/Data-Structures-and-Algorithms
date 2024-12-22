def cr_st():
    stack = []
    return stack

def check_empty(stack):
    return len(stack) == 0


def push(stack, item):
    stack.append(item)
    print("push item: ", item)

def pop(stack):
    if (check_empty(stack)):
        return "Stack is empty"
    
    return stack.pop()


stack = cr_st()
push(stack, str("scme.edu.ps"))
push(stack, str("youtube.com"))
push(stack, str("moodle.scme.edu.ps"))
push(stack, str("google.com"))
push(stack, str("github.com"))
print("stopped item: "+pop(stack))
print("stack after popping an element: "+str(stack))
print("stopped item: "+pop(stack))
print("stack after popping an element: "+str(stack))


class Queue():
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Insert an element into the queue
    def enqueue(self, data):
        if (self.tail == self.k - 1):
            print("The queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = self.tail + 1
            self.queue[self.tail] = data

    # Delete an element from the queue
    def dequeue(self):
        if (self.head == -1):
            print("The queue is empty\n")

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = self.head + 1
            return temp

    def printQueue(self):
        if(self.head == -1):
            print("No element in the queue")

        else:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

