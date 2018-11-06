class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

# Stack: First in, Last out
class Stack:
    def __init__(self):
        self.head = None

    def printStack(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

    def push(self, val):
        newNode = Node(val)
        if (self.head == None):
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode

    def pop(self):
        if (self.head == None):
            print("Error: Stack is empty")
            return -1
        else:
            cur = self.head
            while cur.next:
                if cur.next.next == None:
                    item = cur.next;
                    cur.next = None;
                    return item;

                else:
                    cur = cur.next


stack = Stack()
stack.push(1);
stack.push(2);
stack.push(3);
item = stack.pop();
stack.printStack()
print("Popped: ", item.data)
