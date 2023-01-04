# This algorithm runs in O(n^2) time and O(1) space.

def two_sum(nums, target):
    for lp in range(len(nums)):
        for rp in range(lp+1, len(nums)):
            if nums[lp] + nums[rp] == target:
                return [lp, rp]
