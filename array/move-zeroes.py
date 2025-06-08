class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
        Time Complexity: O(n) (The array is traversed twice)
        Space Complexity: O(1) (In-place modification)
        """
        slow = 0
        # First pass: Move all non-zero elements to the front
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        
        # Second pass: Fill the remaining positions with zeros
        for i in range(slow, len(nums)):
            nums[i] = 0