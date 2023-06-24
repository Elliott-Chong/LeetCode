class Solution:
    def isValid(self, s: str) -> bool:
        currentOpen = []
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:
            if char in matching:
                # char is a closing bracket
                if len(currentOpen) == 0: return False
                if matching[char] == currentOpen[-1]:
                    currentOpen.pop()
                else:
                    return False                    
            else:
                # char is an opening bracket
                currentOpen.append(char)
        return currentOpen == []