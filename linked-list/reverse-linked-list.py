# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Initialize a pointer to keep track of the previous node (starts as None)
        prev = None
        # Initialize a pointer to the current node (starts at the head)
        curr = head

        # Iterate through the list until reaching the end
        while curr:
            # Save the next node before changing the current node's pointer
            next_temp = curr.next
            # Reverse the current node's pointer to point to the previous node
            curr.next = prev
            # Move the prev pointer forward (to the current node)
            prev = curr
            # Move the curr pointer forward (to the next node)
            curr = next_temp

        # At the end, prev will be the new head of the reversed list
        return prev
