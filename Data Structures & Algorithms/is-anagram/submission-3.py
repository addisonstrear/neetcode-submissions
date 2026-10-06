class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChar = {}
        tChar = {}
        for char in s:
            sChar[char] = sChar.get(char,0) + 1
        for char in t:
            tChar[char] = tChar.get(char,0) + 1
        if sChar == tChar:
            return True
        return False
        