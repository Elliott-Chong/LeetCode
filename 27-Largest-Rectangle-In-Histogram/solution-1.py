class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mx = 0
        stack = [] # monotonic increasing stack [[0, 2], [1, 2]]
        for curr_index, curr_height in enumerate(heights):
            start = curr_index
            while stack and curr_height < stack[-1][1]:
                prev_index, prev_height = stack.pop()
                W = curr_index - prev_index
                mx = max(mx, W * prev_height)
                start = prev_index
            stack.append([start, curr_height])
        
        for index, bar in enumerate(stack):
            bar_index, H = bar
            W = len(heights) - bar_index
            mx = max(mx, W * H)
        return mx