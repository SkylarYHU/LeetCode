class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        
        # Iterate over the list with both index and value
        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement number was seen before
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, add the current number and its index to the dictionary
            seen[num] = i
            
        # If no pair found that sums up to target, return empty list
        return []