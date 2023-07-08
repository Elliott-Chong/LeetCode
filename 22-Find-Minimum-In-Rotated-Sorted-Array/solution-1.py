class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        lp, rp = 0, len(nums) - 1

        while lp < rp:
            mp = ( lp + rp ) // 2
            if mp > 0 and nums[mp] < nums[mp - 1]:
                # pivottt
                return nums[mp]

            # check if left half is sorted
            if (nums[mp] >= nums[lp]) and (nums[mp] > nums[rp]):
                lp = mp + 1
            elif nums[rp] > nums[mp]:
                rp = mp - 1
        return nums[lp]