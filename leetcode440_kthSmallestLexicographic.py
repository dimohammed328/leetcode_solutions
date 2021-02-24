import random
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        return self.quickselect(list(range(1,n+1)), k)
    def quickselect(self, arr, k):
        pivot = str(random.choice(arr))
        lowers = [x for x in arr if str(x) < pivot]
        highers = [x for x in arr if str(x) > pivot]
        if len(lowers) >= k:
            return self.quickselect(lowers, k)
        elif k == len(lowers)+1:
            return int(pivot)
        else:
            return self.quickselect(highers, k-len(lowers)-1)
s = Solution()
print(s.findKthNumber(13,6))