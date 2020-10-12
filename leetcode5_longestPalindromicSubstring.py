def longestPalindrome(s: str) -> str:  
        newInput = '$'+''.join([c+'$' for c in s])
        T = [1]*len(newInput)
        start = 0
        end = 0
        i = 0
        while i < len(newInput):
            while start > 0 and end < len(newInput)-1 and newInput[start-1] == newInput[end+1]:
                start -= 1
                end += 1
            T[i] = end-start + 1
            if end == len(newInput) - 1:
                break
            newCenter = end + (1 if i%2==0 else 0)
            j = i+1
            while j <= end:
                T[j] = min(T[i - (j - i)], 2 * (end - j) + 1)
                if (j + T[i - (j - i)]//2) == end:
                    newCenter = j
                    break
                j += 1
            i = newCenter
            end = i + T[i]//2
            start = i - T[i]//2
        m = max(T)
        return(m//2)

print(longestPalindrome("xbabc"))