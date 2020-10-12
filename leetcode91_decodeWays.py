class Solution:
    memo = {}
    def numDecodings(self, s: str) -> int:
        return(self.helper(s, len(s)))
    def helper(self, s, k):
        if k in self.memo:
            return self.memo[k]
        if k == 0:
            return(1)
        n = len(s) - k
        if s[n] == '0':
            return(0)
        numWays = self.helper(s,k-1)
        if k >= 2 and int(s[n:n+2]) <= 26:
            numWays += self.helper(s, k-2)
        self.memo[k] = numWays
        return(numWays)

s = Solution()
print(s.numDecodings("0"))