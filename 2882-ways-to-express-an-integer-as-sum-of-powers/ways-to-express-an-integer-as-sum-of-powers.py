class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        m=int(n**(1/x))
        l=[]
        for i in range(1,m+2):
            p= i**x
            l.append(p)
        dp = [0] * (n + 1)
        dp[0] = 1
        for p in l:
            for s in range(n, p - 1, -1):
                dp[s] = (dp[s] + dp[s - p]) % (10**9+7)

        return dp[n]