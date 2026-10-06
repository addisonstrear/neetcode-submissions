class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to go left to right to find where its furthest apart as well as 
        #tallest height to max volume
        biggestArea = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r-l) * (min(heights[l], heights[r])) 
            if area > biggestArea:
                biggestArea = area
            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] < heights[l]:
                r -=1
        return biggestArea

            