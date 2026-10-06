class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = []
        for char in s:
            if char.isalnum():
                clean.append(char)
        s = "".join(clean)
        l,r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

        