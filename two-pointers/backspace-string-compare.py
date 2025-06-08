class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        Time: O(n + m), where n and m are lengths of s and t
        Space: O(n + m) for the stacks
        """
        def process(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:  # Check if the stack is empty or not
                        stack.pop()
                else:
                    stack.append(char)
            return stack
        return process(s) == process(t)
        