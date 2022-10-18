from math import inf
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        dp = {}
        N = len(nums)

        def helper(idx, n):
            if idx in dp:
                return dp[idx]
            if n == 1:
                return sum(nums[idx:])
            if N-idx == n:
                return max(nums[idx:])
            currSum = 0
            currMin = inf
            for i in range(idx, N-n+1):
                currSum += nums[i]
                nextMin = helper(i+1, n-1)
                currMin = min(currMin, max(currSum, nextMin))
            dp[idx] = currMin
            return currMin
        return helper(0, m)


s = Solution()
print(s.splitArray([2, 3, 1, 3, 4, 3], 5))
