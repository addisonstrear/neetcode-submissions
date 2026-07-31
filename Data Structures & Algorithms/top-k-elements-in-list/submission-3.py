class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        sort = sorted(count.items(), key = lambda pair: pair[1], reverse = True )
        return [pair[0] for pair in sort[:k]]
