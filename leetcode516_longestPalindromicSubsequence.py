def longestPalindromeSubseq(s: str) -> int:
    dp = [[0]*len(s) for _ in range(len(s))]
    for l in range(1,len(s)+1):
        for start in range(0, len(s)-l+1):
            end = start + l-1
            if l <= 2:
                if s[start] == s[end]:
                    dp[start][end] = l
                else:
                    dp[start][end] = 1
            else:
                if s[start] == s[end]:
                    dp[start][end] = 2+dp[start+1][end-1]
                else:
                    dp[start][end] = max(dp[start][end-1], dp[start+1][end])
    return(dp[0][-1])
print(longestPalindromeSubseq('bbbb'))