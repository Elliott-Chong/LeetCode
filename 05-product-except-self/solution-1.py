def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = [1] * len(nums)
        # [1, 1, 1, 1]
        postfix_arr = [1] * len(nums)

        prefix_acc = 1
        for i in range(1, len(nums)):
            prefix_acc *= nums[i-1]
            prefix_arr[i] = prefix_acc

        postfix_acc = 1
        for i in range(len(nums) - 2, -1, -1):
            postfix_acc *= nums[i+1]
            postfix_arr[i] = postfix_acc
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix_arr[i] * postfix_arr[i]
        return re