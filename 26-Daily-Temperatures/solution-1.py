class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] #monotonic decreasing // [[0, 73], [1,74]]

        for curr_index, curr_temp in enumerate(temperatures):
            while stack and stack[-1][1] < curr_temp:
                # no longer monotonic decreasing
                last_index, last_temp = stack.pop()
                answer[last_index] = curr_index - last_index
            stack.append([curr_index, curr_temp])
        return answer