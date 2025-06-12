class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        p_counter = Counter(p)
        window = Counter()
        res = []

        for i in range(len(s)): # i is the index in string s, not the character itself
            window[s[i]] += 1

            if i >= len(p): # If the window size exceeds the length of p, shrink the left boundary
                if window[s[i - len(p)]] == 1: # If the character occurs only once in the window
                    del window[s[i - len(p)]]
                else:
                    window[s[i - len(p)]] -= 1
            
            if window == p_counter:
                res.append(i - len(p) + 1)
        return res