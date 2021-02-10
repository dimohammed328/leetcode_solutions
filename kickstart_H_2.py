def maxCoins(n,mat):
    l = n*2-1
    offset = l // 2
    dp = [0]*l
    for i in range(n):
        for j in range(n):
            dp[i-j+offset] += mat[i][j]
    return(max(dp))
c = int(input())
for i in range(c):
    n = int(input())
    mat = []
    for j in range(n): 
        l = input()
        mat += [[int(x) for x in l.split(' ')]]
    print('Case #%d: %d' % (i+1, maxCoins(n,mat)))
