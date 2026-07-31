class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ''
        for char in s:
            if char.isalnum() == True:
                clean = clean + char.lower()
        # need to drop punctuation and capitals

        start, end = 0, len(clean) - 1
        if clean == '':
            return True

        for i in range(int(len(clean)/2)):
            if clean[start] == clean[end]:
                start += 1
                end -= 1
                continue
            else:
                return False
        return True