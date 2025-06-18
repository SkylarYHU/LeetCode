class MyQueue(object):

    def __init__(self):
        # Initialize two stacks:
        # stack_in is used to push new elements (normal stack push)
        # stack_out is used for pop / peek operations (reversed to simulate queue order)
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # Push element x into the input stack
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        # If stack_out is empty, move elements from stack_in to stack_out
        self.move()
        # Pop the top element from stack_out (simulating dequeuing from the front)
        return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        # Make sure stack_out has elements to peek
        self.move()
        # Return the front element without removing it
        return self.stack_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        # The queue is empty only when both stacks are empty
        return not self.stack_in and not self.stack_out

    def move(self):
        # Only move elements if stack_out is empty
        # This simulates reversing the order from stack_in (LIFO) to stack_out (FIFO)
        # For example, stack_in = [1, 2, 3] → stack_out = [3, 2, 1], then popping gives 1, 2, 3
        if not self.stack_out:
            # Transfer all elements from stack_in to stack_out
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()