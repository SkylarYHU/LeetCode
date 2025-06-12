# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        fast = dummy
        slow = dummy

        # Move fast pointer n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # After this loop, slow will be just before the node to remove
        while fast.next:
            fast = fast.next # fast will reach None
            slow = slow.next

        # Remove the nth node from the end by skipping it
        slow.next = slow.next.next

        # Return the head of the updated list
        return dummy.next