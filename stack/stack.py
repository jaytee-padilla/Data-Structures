from doubly_linked_list import DoublyLinkedList

"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
as the underlying storage structure.
Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
implementing a Stack?
"""

"""
array implementation of stack
"""
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
#         self.length = 0

#     def __len__(self):
#         return self.length

#     def push(self, value):
#         self.length += 1
#         self.storage.append(value)

#     def pop(self):
#         if self.length == 0:
#             return None
#         else:
#             self.length -= 1
#             return self.storage.pop()

"""
Linked List implementation of stack
"""

class Stack:
  def __init__(self):
    self.size = 0
    self.storage = DoublyLinkedList()
    self.length = 0

  def __len__(self):
    return self.length

  def push(self, value):
    self.length += 1
    self.storage.add_to_tail(value)

  def pop(self):
    if self.length == 0:
      return None
    else:
      self.length -= 1
      return self.storage.remove_from_tail()