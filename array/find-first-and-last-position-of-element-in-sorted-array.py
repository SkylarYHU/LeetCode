class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        Find the starting and ending positions of the target value in the array
        If nums = [5,7,7,8,8,8,10] and target = 8, it should return [3, 5].
        """
        def find_first(nums, target):
            left, right = 0, len(nums) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    first = mid
                    right = mid - 1 # Found target, but continue searching left for the first occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return first
        
        def find_last(nums, target):
            left, right = 0, len(nums) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    last = mid
                    left = mid + 1 # Found target, but continue searching right for the last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return last
        
        return [find_first(nums, target), find_last(nums, target)]
        