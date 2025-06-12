class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        for char in t:
            # If a character is not in the count dictionary,
            # it means t contains a character not in s;
            # or if the character count is already 0, 
            # it means t has more of this character than s does.
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1

        # If all characters are successfully matched,
        # return True, meaning t is an anagram of s.
        return True