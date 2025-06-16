class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)  # Convert the string to a list for in-place modifications

        # For every 2k characters in the string, reverse the first k characters
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])  # Reverse the first k characters in the current 2k block
        
        return ''.join(s)  # Convert the list back to a string and return