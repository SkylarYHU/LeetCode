from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        dq = deque()

        for i in range(len(nums)):
            # Remove indices that are out of the window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            # Maintain decreasing order: pop smaller elements from the back
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            # When window is full, add the maximum to result
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result