class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Edge case: if needle is an empty string, return 0
        if not needle:
            return 0

        # 1. Build the LPS (Longest Prefix Suffix) array for the pattern
        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0  # length of the previous longest prefix suffix
            i = 1  # start from the second character

            while i < len(pattern):
                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]  # fallback to previous LPS
                    else:
                        lps[i] = 0
                        i += 1
            return lps

        lps = build_lps(needle)

        # 2. Use the LPS array to perform KMP search
        i = 0  # index for haystack
        j = 0  # index for needle

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lps[j - 1]  # use LPS to skip characters
                else:
                    i += 1

            # full match found
            if j == len(needle):
                return i - j  # return the start index of the match

        return -1  # no match found