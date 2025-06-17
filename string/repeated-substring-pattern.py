class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def build_lps(pattern):
            length = 0
            lps = [0] * len(pattern)
            i = 1

            # Build the LPS (Longest Prefix Suffix) array for the pattern
            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        # If mismatch after some matches, fall back to previous longest prefix
                        length = lps[length - 1]
                    else:
                        # No prefix suffix match, set LPS to 0 and move forward
                        lps[i] = 0
                        i += 1
            return lps

        lps = build_lps(s)
        len_s = len(s)
        longest = lps[-1]  # Get the length of the longest prefix which is also a suffix for the entire string
        
        # If longest == 0, it means no proper prefix-suffix found
        # longest > 0 means there is some repeated prefix and suffix, indicating possible repeated substring
        # len_s % (len_s - longest) == 0 checks if the total length can be divided evenly by the length of the repeating unit
        # The length of the repeating substring is (len_s - longest)
        return longest > 0 and len_s % (len_s - longest) == 0

