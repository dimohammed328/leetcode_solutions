def maxProfit(k, prices):
        dp = [[0]*len(prices) for _ in range(k+1)]
        for i in range(1,k+1):
            for j in range(1,len(prices)):
                maxP = 0
                for m in range(j):
                    maxP = max(maxP, prices[j]-prices[m]+dp[i-1][m])
                dp[i][j] = max(maxP, dp[i][j-1])
        return dp[-1][-1]

print(maxProfit(2, [2,4,1]))

