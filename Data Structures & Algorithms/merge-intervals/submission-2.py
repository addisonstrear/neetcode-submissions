class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final = []
        # for each interval, check if the lower bound lies inside previous interval
        #if it does, new upper bound of overlapping interval is upper bound of      
        # current interval. Otherwise, append to final and start new lower and  
        #upper at the next iteration of current interval
        intervals.sort()
        upperBound = intervals[0][1]
        lowerBound = intervals[0][0]
        
        for i in range(1, len(intervals)):

            currentInt = intervals[i]
            
            if currentInt[0] <= upperBound:
                upperBound = max(upperBound,currentInt[1])
                lowerBound = min(lowerBound, currentInt[0])
            else:
                final.append([lowerBound,upperBound])
                lowerBound = currentInt[0]
                upperBound = currentInt[1]

        final.append([lowerBound, upperBound])
        return final

        