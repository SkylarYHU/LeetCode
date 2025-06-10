class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter, defaultdict

        if not s or not t:
            return ""

        need = Counter(t)  # Count of required characters in t
        window = defaultdict(int)  # Current window character counts
        have, need_count = 0, len(need)  # have: how many required characters are fully matched

        res = ""
        min_len = float('inf')
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] += 1  # Add current character to the window

            # If the current character is needed and now fully matched, increment 'have'
            if char in need and window[char] == need[char]:
                have += 1

            # Try to shrink the window from the left while it's valid
            while have == need_count:
                # Update result if the current window is smaller
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    res = s[left:right + 1]

                # Shrink the window from the left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return res
