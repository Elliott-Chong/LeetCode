class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lp = 0
        max_length = 0
        currCharSet = set()
        for rp in range(len(s)):
            while s[rp] in currCharSet:
                currCharSet.remove(s[lp])
                lp += 1
            currCharSet.add(s[rp])
            currWindowLength = rp - lp + 1
            if currWindowLength > max_length:
                max_length = currWindowLength
        return max_length

        

