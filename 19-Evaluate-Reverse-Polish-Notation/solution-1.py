class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = '*+/-'
        stack = []

        for token in tokens:
            if token not in operations:
                # token is a normal integer
                stack.append(token)
            else:
                # token is an operator
                last = int(stack.pop())
                second_last = int(stack.pop())

                eval = 0
                if token == '*':
                    eval = second_last * last
                elif token == '-':
                    eval = second_last - last
                elif token == '+':
                    eval = second_last + last
                else:
                    eval = second_last / last

                stack.append(eval)
        return int(stack[-1])