class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(output, current_string, numOpen, numClose):
            if len(current_string) == n * 2:
                output.append(current_string)
                return
            
            if numOpen < n:
                backtrack(output, current_string + '(', numOpen + 1, numClose)
            if numClose < numOpen:
                backtrack(output, current_string + ')', numOpen, numClose + 1)
            
        backtrack(output, '', 0, 0)
        return output