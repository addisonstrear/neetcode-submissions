class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix = [1]
        suffix = [1] * len(nums)
        running = 1
        final = []
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] * nums[i-1])
        for j in range(len(nums) - 1, -1, -1):
            suffix[j] = running 
            running = running * nums[j]
        for k in range(len(nums)):
            final.append(prefix[k] * suffix[k])
        return final
            

            

