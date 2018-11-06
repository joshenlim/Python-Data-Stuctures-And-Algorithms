class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listPrint(self):
        cur = self.head
        while cur != None:
            print(cur.data)
            cur = cur.next

    def insertAtBeginning(self, val):
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self, val):
        newNode = Node(val)
        if (self.head == None):
            self.head = newNode
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = newNode

    def removeNode(self, val):
        if (self.head == None):
            print("Error: Linked list is empty")
            return -1
        elif (self.head.data == val):
            self.head = self.head.next
            return
        else:
            cur = self.head
            while cur.next:
                if (cur.next.data == val):
                    cur.next = cur.next.next
                    return
                else:
                    cur = cur.next
            print("Error: Unable to find item in linked list")
            return -1


########################################################

list = LinkedList();
list.insertAtBeginning(1);
list.insertAtBeginning(2);
list.insertAtEnd(3)

list.removeNode(4)
list.listPrint()
