# [100, 102, 101, 1, 2]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        num_set = set(nums)

        for num in nums:
            # is this num the start of a new seq?
            if num - 1 not in num_set:
                # this num is the start of a new seq
                local_length = 1
                while num + 1 in num_set:
                    local_length += 1
                    num += 1
                # this is the end of the seq
                max_length = max(max_length, local_length)
        return max_length
        

                
        

