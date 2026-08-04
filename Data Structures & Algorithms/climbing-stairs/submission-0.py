class Solution:
    def climbStairs(self, n: int) -> int:
        #fibonacci sequence, f(n) = f(n-1) + f(n-2) for n = # steps
        #return f(n)
        if n == 1:
            return 1
        prev = 1
        current = 2
        for i in range (3, n+1):
            nextstep = prev + current
            prev = current
            current = nextstep
        return current
            

           

