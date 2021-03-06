from doubly_linked_list import DoublyLinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
as the underlying storage structure.
Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
What would that look like? How many Stacks would you need? Try it!
"""

"""
array implementation of queue
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#         self.length = 0
    
#     def __len__(self):
#         return self.length

#     def enqueue(self, value):
#         self.length += 1
#         self.storage.append(value)

#     def dequeue(self):
#         if self.length == 0:
#             return None
#         else:
#             self.length -= 1
#             return self.storage.pop(0)

"""
Linked List implementation of queue
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
        self.length = 0

    def __len__(self):
        return self.length

    def enqueue(self, value):
        if self.length == 0:
            self.length += 1
            self.storage.add_to_head(value)
        else:
            self.length += 1
            self.storage.add_to_tail(value)

    def dequeue(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.length -= 1
            return self.storage.remove_from_head()
        else:
            self.length -= 1
            return self.storage.remove_from_head()