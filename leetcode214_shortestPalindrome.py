import math
def shortestPalindrome(s: str) -> str:
        newInput = s + '$' + s[::-1]
        kmp = [0]*len(newInput)
        j =  0
        i = 1
        while i < len(newInput):
            if newInput[i] == newInput[j]:
                kmp[i] = j+1
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = kmp[j-1]
        maxLen = kmp[-1]
        return(s[:maxLen-1:-1]+s)
print(shortestPalindrome('aaacecaaaa'))
