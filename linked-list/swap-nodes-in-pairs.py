# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # Create a dummy node with value 0
        dummy.next = head    # Link dummy to the head of the original list
        prev = dummy         # Initialize a helper pointer 'prev' to dummy
            
        # Loop while there are at least two nodes to swap
        while prev.next and prev.next.next:
            first = prev.next        # First node of the pair
            second = first.next      # Second node of the pair
        
            first.next = second.next # Step 1: Point first to the node after second
            second.next = first      # Step 2: Point second to first (swap them)
            prev.next = second       # Step 3: Connect previous part to second
        
            prev = first             # Move prev to the end of the swapped pair
        
        # Return the new head of the list
        return dummy.next