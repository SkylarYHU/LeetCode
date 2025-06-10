class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix = [0] # Initialize prefix list with 0, representing sum of zero elements
        for num in nums:
            # Add current number to the last prefix sum and append to prefix list
            self.prefix.append(self.prefix[-1] + num)
    def sumRange(self, left, right):
        # Return the sum of elements from index left to right inclusive
        return self.prefix[right + 1] - self.prefix[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
