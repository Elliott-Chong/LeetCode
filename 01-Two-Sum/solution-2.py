# This algorithm runs in O(n) time and O(n) space.

def two_sum(nums, target):
    # seen is a hashmap that maps values to their indices
    seen = {}
    for index, num in enumerate(nums):
        complement = target - num
        if (complement in seen):
            return [seen[complement], index]
        seen[num] = index
