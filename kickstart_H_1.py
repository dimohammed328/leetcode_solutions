def count(s):
    kicks = 0
    totalCount = 0
    for i in range(len(s)):
        if i <= len(s)-4:
            if s[i:i+4] == 'KICK':
                kicks += 1
        if i <= len(s)-5:
            if s[i:i+5] == 'START':
                totalCount += kicks
    return totalCount
numCases = int(input())
for i in range(numCases):
    s = input()
    print('Case #%d: %d' % (i+1, count(s)))