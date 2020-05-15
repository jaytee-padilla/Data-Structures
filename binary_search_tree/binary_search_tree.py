"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the incoming value is less than the current node's value
        if value < self.value:
            # go left
            # how do we know when we need to recurse again,
            # or when to stop?
            if not self.left:
                # self.left doesn't exist, therefore we can park the value in this spot
                self.left = BSTNode(value)
            else:
                # can't park value in this spot
                # keep searching
                self.left.insert(value)
        else:
            # go right
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # when we start searching, self will be the root
        # compare the target against self
        # 
        # Criteria for returning False: we know we need to go in one direction
        # but there's nothing in the left or right direction 
        if target == self.value:
            return True
        if target < self.value:
            # go left if left is a BSTNode
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # go right if right is a BSTNode
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # keep going right until there are no more nodes on the right side
        if not self.right:
            return self.value
        # otherwise, keep going right
        return self.right.get_max()

    def iterative_get_max(self):
        current_max = self.value

        current = self

        #traverse data structure
        while current is not None:
            if current.value > current_max:
                current_max = current.value
            # update our current_max var if a larger value is found
            current = current.right

        return current_max

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the fn on the value at this node
        fn(self.value)

        # pass this function to the left child
        if self.left:
            self.left.for_each(fn)
        # pass this function to the right child
        if self.right:
            self.right.for_each(fn)

    def iterative_for_each(self, fn):
        stack = []

        # add root node
        stack.append(self)

        # loop so long as the stack still has elements
        while len(stack) > 0:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if left node exists, continue going down that branch
        # if right node exists, continue going down that branch
        if node: # does the node exist
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.in_order_print(bst)
# bst.value