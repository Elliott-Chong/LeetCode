class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            num = nums[i]
            if i > 0 and nums[i - 1] == num: continue
            lp = i + 1
            rp = len(nums) - 1
            while lp < rp:
                threeSum = nums[lp] + nums[rp] + num
                if threeSum < 0:
                    lp += 1
                elif threeSum > 0:
                    rp -= 1 
                else:
                    res.append([num, nums[lp], nums[rp]])
                    lp += 1
                    while nums[lp - 1] == nums[lp] and lp < rp:
                        lp += 1
        return res

