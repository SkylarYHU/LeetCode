class Solution:
    def evalRPN(self, tokens):
        from operator import add, sub, mul
        stack = []

        # Define operator functions
        def divide(a, b):
            # Truncate toward zero manually
            return int(a / b) if a * b >= 0 else -(-a // b)

        # Map each operator to the corresponding function
        ops = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': divide
        }

        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                result = ops[token](a, b)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack[0]


