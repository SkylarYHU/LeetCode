# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # If the list is empty or has only one node, there can't be a cycle
        if not head or not head.next:
            return None
        
        slow = head
        fast = head

        # Move slow by 1 step and fast by 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If slow and fast meet, there is a cycle
            if slow == fast:
                # Move slow back to the head
                slow = head
                # Move both pointers one step at a time until they meet again
                # The meeting point will be the start of the cycle
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # Return the node where the cycle begins

        # If no cycle is detected
        return None