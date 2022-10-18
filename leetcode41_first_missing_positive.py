from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] - 1 != i and nums[i] > 0 and nums[i] <= len(nums):
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        for i, x in enumerate(nums):
            if x != i+1:
                return i+1
        return len(nums)+1


# s = Solution()
# print(s.firstMissingPositive([3, 4, -1, 1]))
N = 6
x = list(range(1, N+1))
sum = 0
for i in x:
    for j in x:
        sum += max(i, j)
print(sum/(N*N))
