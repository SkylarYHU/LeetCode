# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0) # Create a dummy head node to simplify handling cases where the head node needs to be removed
        dummy.next = head # Link the dummy node to the original head of the list; now the list starts from dummy, but real data starts from head
        current = dummy # Initialize the current pointer to start from dummy

        while current.next: # Traverse the list as long as there is a next node
            if current.next.val == val: # If the next node's value equals the target value to be removed
                current.next = current.next.next # Skip the next node by linking current node to the node after next
            else:
                current = current.next # Otherwise, move current forward to the next node
        return dummy.next # Return the new head of the list, which is the node after dummy