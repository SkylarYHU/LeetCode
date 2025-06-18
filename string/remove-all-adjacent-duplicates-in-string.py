class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []  # Use a stack to keep processed characters for easy comparison of adjacent duplicates

        for c in s:  # Iterate through each character in the string
            if stack and stack[-1] == c:
                # If the stack is not empty and the top element is the same as the current character,
                # it's a duplicate, so we remove the top of the stack
                stack.pop()
            else:
                # If not a duplicate, push the current character onto the stack
                stack.append(c)
        
        # Join all remaining characters in the stack into the final string and return
        return ''.join(stack)
