class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()  # Sort the array to simplify skipping duplicates and enable two-pointer technique
        res = []

        for i in range(len(nums) - 2):  # Loop until the third-last element (since we need triplets)
            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1  # Use two pointers to find the remaining two elements

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1  # Sum is too small, move left pointer to the right
                elif total > 0:
                    right -= 1  # Sum is too large, move right pointer to the left
                else:
                    res.append([nums[i], nums[left], nums[right]])  # Found a valid triplet

                    # Skip duplicate values for the left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate values for the right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move both pointers to look for the next potential triplet
                    left += 1
                    right -= 1

        return res
