class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        # Create a dictionary `anagrams`
        # The key is the sorted version of each word (e.g., "aet")
        # The value is a list of words that match this key (e.g., ["eat", "tea", "ate"])
        # defaultdict(list) automatically creates an empty list if the key doesn't exist
        anagrams = defaultdict(list) 

        for word in strs:
            # Sort the characters in the word, then join them to form the key
            key = ''.join(sorted(word))
            # Append the word to the corresponding anagram group
            anagrams[key].append(word)
        
        # Return all the grouped anagrams as a list of lists
        return list(anagrams.values())