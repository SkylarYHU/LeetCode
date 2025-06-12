# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        # If either linked list is empty, there can be no intersection
        if not headA or not headB:
            return None

        # Initialize two pointers, pA and pB, at the heads of A and B respectively
        # These pointers will traverse the two lists
        pA, pB = headA, headB

        # Continue looping until the two pointers meet
        # When pA == pB, it means either intersection node is found or both reached the end (None)
        while pA != pB:
            # Move pA to the next node; if pA reaches the end, redirect it to headB
            pA = pA.next if pA else headB

            # Move pB to the next node; if pB reaches the end, redirect it to headA
            pB = pB.next if pB else headA

            # By switching heads when reaching the end,
            # both pointers traverse the combined length of both lists
            # ensuring they meet at the intersection or end at None together

        # Return either the intersection node or None if no intersection exists
        return pA
