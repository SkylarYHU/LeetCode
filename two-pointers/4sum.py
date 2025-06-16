class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to make it easier to skip duplicates and use two pointers
        res = []  # This will store the final list of unique quadruplets

        for i in range(len(nums) - 3):  # First pointer, loop until the 4th last element
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values for the first number
            
            for j in range(i + 1, len(nums) - 2):  # Second pointer
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicate values for the second number
                
                left = j + 1  # Third pointer (left)
                right = len(nums) - 1  # Fourth pointer (right)

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]  # Sum of four numbers

                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])  # Found a valid quadruplet

                        # Skip duplicate values for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        
                        # Skip duplicate values for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # Move both pointers after finding a valid quadruplet
                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1  # If sum is too small, move left pointer to the right

                    else:
                        right -= 1  # If sum is too large, move right pointer to the left

        return res  # Return the list of unique quadruplets

                        
