def change(amount, coins):
    dp = {}
    return(helper(amount,coins,dp))
def helper(amount, coins, dp):
    if amount in dp:
        return(dp[amount])
    if amount == 0:
        return(1)
    numWays = 0
    idx = 0
    while idx < len(coins) and coins[idx] <= amount:
        numWays += helper(amount-coins[idx],coins,dp)
        idx += 1
    dp[amount] = numWays
    return(numWays)

print(change(5, [1,2,5]))