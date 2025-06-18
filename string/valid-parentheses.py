class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []  # Stack to keep track of opening brackets
        mapping = {')': '(', '}': '{', ']': '['}  # Map of closing to opening brackets
        
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element from the stack if it's not empty,
                # otherwise assign a dummy value '#' to avoid errors
                top_element = stack.pop() if stack else '#'
                # If the popped element doesn't match the expected opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # If it is an opening bracket, push it onto the stack
                stack.append(char)
        
        # In the end, if the stack is empty, all brackets matched correctly
        return not stack


        