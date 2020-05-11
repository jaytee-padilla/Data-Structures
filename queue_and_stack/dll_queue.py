import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()
        self.head = None
        self.last = None

    def enqueue(self, value):
        if self.last is None: 
            self.head = ListNode(value) 
            self.last = self.head
            self.size += 1
        else: 
            self.last.next = ListNode(value) 
            self.last.next.prev = self.last 
            self.last = self.last.next
            self.size += 1

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return temp 

    def len(self):
        return self.length
