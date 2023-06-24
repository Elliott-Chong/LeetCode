class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ''

        window = {}
        original = {}

        for char in t:
            original[char] = original.get(char, 0) + 1
        
        res = [-1, -1]
        res_len = float('inf')

        have = 0
        need = len(original)

        lp = 0 
        for rp in range(len(s)):
            char = s[rp]
            window[char] = window.get(char, 0) + 1
            if char in original:
                if window[char] == original[char]:
                    have += 1

            while have == need:
                if (rp - lp + 1) < res_len:
                    res = [lp, rp]
                    res_len = rp - lp + 1
                window[s[lp]] -= 1
                if s[lp] in original:
                    if window[s[lp]] < original[s[lp]]:
                        have -= 1
                lp += 1
        if res_len == float('inf'):
            return ''
        res_lp , res_rp = res
        return s[res_lp : res_rp + 1]

