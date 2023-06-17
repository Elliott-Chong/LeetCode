class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        lp = 0

        original_char_set = [0] * 26
        window_char_set = [0] * 26

        for char in s1:
            original_char_set[ord(char) - 97] += 1
        
        for i in range(len(s1)):
            window_char_set[ord(s2[i]) - 97] += 1
        
        for rp in range(len(s1), len(s2)):
            if window_char_set == original_char_set:
                return True
            window_char_set[ord(s2[rp]) - 97] += 1
            window_char_set[ord(s2[lp]) - 97] -= 1

            lp += 1
            rp += 1
        
        return window_char_set == original_char_set
