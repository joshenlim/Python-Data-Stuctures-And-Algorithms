class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# Queue: First in, First out
class Queue:
    def __init__(self):
        self.head = None

    def printQ(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

    def enqueue(self, val):
        newNode = Node(val)
        if (self.head == None):
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode

    def dequeue(self):
        if (self.head == None):
            print("Error: Queue is empty")
            return -1
        else:
            item = self.head
            self.head = self.head.next
            return item


queue = Queue()
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
item = queue.dequeue();
queue.printQ()
print("Dequeued: ", item.data)
