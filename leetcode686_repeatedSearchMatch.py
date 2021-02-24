import math
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        arr = self.kmp(b)
        times = math.ceil(len(b)/len(a))+1
        s = a*times
        i = 0
        j = 0
        while i < len(s):
            if s[i] == b[j]:
                j += 1
                i += 1
            else:
                if j > 0:
                    j = arr[j-1]
                else:
                    i += 1
            if j == len(b):
                return i-j-1
        return -1
    def kmp(self, pattern):
        arr = [0]*len(pattern)
        i = 1
        j = 0
        while i < len(pattern):
            if pattern[i] == pattern[j]:
                arr[i] = j+1
                i += 1
                j += 1
            else:
                if j > 0:
                    j = arr[j-1]
                    while j > 0 and pattern[j] != pattern[i]:
                        j = arr[j-1]
                else:
                    i += 1
        return arr
s = Solution()
print(s.repeatedStringMatch('abcd', 'cdabcdab'))