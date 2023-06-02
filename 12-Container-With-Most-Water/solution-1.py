class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        max_area = 0


        while lp < rp:
            left_height = height[lp]
            right_height = height[rp]
            width = rp - lp
            if left_height < right_height:
                area = left_height * width 
                max_area = max(max_area, area)
                lp += 1
            elif left_height >= right_height:
                area = right_height * width
                max_area = max(max_area, area)
                rp -= 1
        return max_area
            

            