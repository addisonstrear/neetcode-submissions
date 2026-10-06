class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        best = 0
        current = 0
        streak = set()
        for i in range(len(s)):
            while s[i] in streak:
                streak.remove(s[l])
                l+=1
                current -= 1
            streak.add(s[i])
            current += 1
            if current > best:
                best = current
        return best
            
            
                
                



