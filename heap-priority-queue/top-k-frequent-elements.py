from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = Counter(nums)
        # Step 1: Count the frequency of each number using Counter
        # Example: Counter([1,1,1,2,2,3]) -> {1: 3, 2: 2, 3: 1}

        # Step 2: Use heapq.nlargest to get the k elements with the highest frequency
        # count.items() returns (element, frequency) pairs, e.g., [(1, 3), (2, 2), (3, 1)]
        # key=lambda x: x[1] tells nlargest to compare by frequency (x[1])
        # Example result: [(1, 3), (2, 2)]

        # Step 3: Extract only the element part from the (element, frequency) pairs
        return [item for item, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
