class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0 # result to return
        lp = 0
        charCount = {}
        for rp in range(len(s)):
            current_char = s[rp]
            charCount[current_char] = charCount.get(current_char, 0) + 1
            window_length = rp - lp + 1
            while window_length - max(charCount.values()) > k:
                charCount[s[lp]] -= 1
                lp += 1
                window_length = rp - lp + 1
            max_length = max(max_length, window_length)
        return max_length