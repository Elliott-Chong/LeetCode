class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1
        while lp < rp:
            current_sum = numbers[lp] + numbers[rp]
            if current_sum == target:
                return [lp + 1, rp + 1]
            if current_sum < target:
                lp += 1
            elif current_sum > target:
                rp -= 1
        return []
            