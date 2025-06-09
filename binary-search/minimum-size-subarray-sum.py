class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        hint: slide window
        """
        left = 0
        total = 0
        min_len = float('inf') # Initialize the minimum length to infinity

        for right in range(len(nums)): # Expand the window by moving the right pointer
            total += nums[right]

            # Shrink the window as small as possible while the total is still >= target
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        return 0 if min_len == float('inf') else min_len # If min_len was never updated, return 0. 