class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """ 
        from collections import defaultdict # Dictionary to count fruit types in the window
        fruit_count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1 # Add the current fruit to the window

            # Shrink the window if we have more than 2 types of fruits
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1 # Remove one fruit from the left
                if fruit_count[fruits[left]] == 0: # Remove the type if count is 0
                    del fruit_count[fruits[left]]
                left += 1
            max_fruits = max(max_fruits, right - left + 1)
        return max_fruits