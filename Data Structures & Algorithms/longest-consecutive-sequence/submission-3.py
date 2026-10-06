class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(nums)
        currentMax = 1
        bigMax = 1
        if len(sort) == 0:
            return 0
        for i in range(1,len(sort)):
            if sort[i] == sort[i-1]:
                continue
            if sort[i] == sort[i-1] + 1 :
                currentMax += 1
                if currentMax > bigMax:
                    bigMax = currentMax
            else:
                currentMax = 1
        return bigMax
            
        