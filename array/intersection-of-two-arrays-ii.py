class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        count = Counter(nums1)
        result = []

        for num in nums2:
            # If the number exists in nums1 and hasn't been used up
            if count[num] > 0:
                result.append(num)
                # Decrease the count to avoid overuse
                count[num] -= 1
        return result
