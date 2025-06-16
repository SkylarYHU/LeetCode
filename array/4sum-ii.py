class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        from collections import defaultdict
        count = defaultdict(int)

        # Compute all possible sums of elements from nums1 and nums2
        for a in nums1:
            for b in nums2:
                count[a + b] += 1  # Store the sum of a + b and how many times it appears

        ans = 0  # Count the number of valid tuples

        # Check if the negative sum of elements from nums3 and nums4 exists in the map
        for c in nums3:
            for d in nums4:
                ans += count[-(c + d)]  # If the complement exists in 'count', add its frequency to the answer

        return ans
