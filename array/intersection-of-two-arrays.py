class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count = {}          
        result = set()       # Use a set to store the intersection result (unique elements only)

        for num in nums1:
            count[num] = True    # Mark each number in nums1 as seen

        for num in nums2:
            if num in count:     # If the number is also in nums1
                result.add(num)  # Add it to the result set
        
        return list(result)
