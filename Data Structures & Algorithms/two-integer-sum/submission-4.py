class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            for k in range(i+1, len(nums)):
                if nums[k] == diff:
                    return [i, k]

