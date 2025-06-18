from collections import deque  # Use deque to implement queue

class MyStack(object):

    def __init__(self):
        # Initialize two queues
        self.q1 = deque()
        self.q2 = deque()
        
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.q2.append(x)  # First, append the new element to the empty queue q2
        # Transfer all elements from q1 to q2 one by one,
        # so the new element is positioned at the front (top of the stack)
        while self.q1:
            # popleft() removes and returns an element from the left/front of the deque (queue)
            self.q2.append(self.q1.popleft())  # After this, q1 becomes empty
        # Swap q1 and q2, so q1 becomes the main queue with correct order (front is top of stack),
        # and q2 becomes empty, ready for next push
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        :rtype: int
        """
        return self.q1.popleft()  # The front of q1 is the top element of the stack
        
    def top(self):
        """
        :rtype: int
        """
        return self.q1[0]  # Return the front element without removing it
        
    def empty(self):
        """
        :rtype: bool
        """
        return not self.q1  # Return True if q1 is empty, else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
