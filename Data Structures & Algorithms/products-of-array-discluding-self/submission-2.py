class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        earlier = [1] * len(nums)
        later = [1] * len(nums)
        final = [1] * len(nums)
        for i in range(1,len(nums)):
            #earlier vals:
            runningProd = nums[i-1]
            earlier[i] = earlier[i-1] * runningProd

            runningendProd = nums[len(nums)-i]
            later[len(nums)-i-1] = later[len(nums)-i] * runningendProd

        for i in range(0,len(nums)):
            final[i] = earlier[i] * later[i]
        return final
        
        
        