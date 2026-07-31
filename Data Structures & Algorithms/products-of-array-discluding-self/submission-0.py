class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        final = [1] * length
        before = 1
        for i in range(length):
            final[i] = before
            before *= nums[i]
        
        after = 1
        for i in range(length-1, -1, -1):
            final[i] *= after
            after *= nums[i]

        return final
