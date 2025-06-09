class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        Time: O(n) – each number is processed once
        Space: O(n) – for the result array
        """
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        # We cannot determine the position of the smallest squared value at the beginning,
        # but we can determine the position of the largest one.
        # Therefore, we fill the result array from the end.
        pos = n - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]): # Don't forget abs()
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1
        return result

        