# Define a singly linked list node class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Define the main class MyLinkedList to implement various linked list operations
class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode(0)  # Create a dummy head node, not real data, just to simplify operations
        self.size = 0  # Track the actual length of the linked list

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        # If index is out of bounds (negative or beyond the current size), return -1 directly
        if index < 0 or index >= self.size:
            return -1
            
        curr = self.head.next  # Point to the first real node (skip the dummy head)
        # Traverse the list index times to find the target node
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)  # Insert a node at the head, equivalent to inserting at index 0

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)  # Insert a node at the tail, equivalent to inserting at the current length

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # If index is greater than the current size (too far), do not insert
        if index > self.size:
            return
        # If index is negative, treat it as 0 (insert at head)
        if index < 0:
            index = 0
        
        # Start from dummy head, traverse index times to find the node before insertion point (prev)
        prev = self.head
        for _ in range(index):
            prev = prev.next
        
        # Standard insertion steps:
        # First, point the new node's next to prev's next node
        # Then, point prev's next to the new node
        # Finally, update the linked list size
        new_node = ListNode(val)  # Create a new ListNode with value val, next is None by default
        new_node.next = prev.next  # Link new_node's next to prev's next node (still connected)
        prev.next = new_node       # Connect prev to the new_node, insertion completed
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        # If the deletion index is invalid (out of range), skip
        if index < 0 or index >= self.size:
            return
        # Find the node before the one to delete
        # Link prev.next directly to the node after the target node, completing deletion
        # Update the linked list size
        prev = self.head
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)