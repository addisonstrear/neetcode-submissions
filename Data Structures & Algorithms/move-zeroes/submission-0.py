class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        w = 0
        for i in range(0,len(nums)):
           
            if nums[i] != 0:
                x = nums[w]
                nums[w] = nums[i]
                nums[i] = x
                w+=1
        

        