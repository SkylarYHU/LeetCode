class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop two operands from the stack
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Core logic: perform integer division with truncation toward zero
                    # Python's a / b is float division, e.g., -6 / 132 = -0.045...
                    # int(a / b) truncates toward zero (e.g., int(-0.045) = 0)
                    # If a and b have the same sign (a * b >= 0), int(a / b) is safe
                    # If a and b have opposite signs, use -(-a // b) to force truncation toward zero
                    stack.append(int(a / b) if (a * b) >= 0 else -(-a // b))
            else:
                # Convert number token to int and push onto the stack
                stack.append(int(token))

        # Final result is the only item left in the stack
        return stack[0]


