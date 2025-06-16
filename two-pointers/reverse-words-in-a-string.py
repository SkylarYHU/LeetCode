class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split() # Split the string by spaces to get the list of words
        words.reverse()
        return ' '.join(words) # Join the words with a single space and return the result.