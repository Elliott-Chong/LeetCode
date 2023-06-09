class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        lp = 0
        rp = len(height) - 1
        res = 0
        maxL = height[lp]
        maxR = height[rp]

        while lp < rp:
            if maxL < maxR:
                lp += 1
                maxL = max(maxL, height[lp])
                res += maxL - height[lp]
            else:
                rp -= 1 
                maxR = max(maxR, height[rp])
                res += maxR - height[rp]
        return res
