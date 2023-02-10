# this solution will run in O(n) time and O(n) space
class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        for alphabet in nums:
            count[alphabet] = count.get(alphabet, 0) + 1
        freq = []
        for i in range(0, len(nums) + 1):
            # 0, 1, 2, 3, 4, 5, 6, 7
            freq.append([])
        # [ [], [], [], [], [], [], [], [] ]
        for alphabet, occurance in count.items():
            freq[occurance].append(alphabet)

        res = []

        for reversing_index in range(len(nums), 0, -1):
            small_array = freq[reversing_index]
            for alphabet in small_array:
                res.append(alphabet)
                if len(res) == k:
                    return res
