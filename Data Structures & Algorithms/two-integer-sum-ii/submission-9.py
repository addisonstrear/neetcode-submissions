class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = set()
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return[numbers.index(diff)+1, i+1]
            else:
                seen.add(num)
            
            