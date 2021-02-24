class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        i = 1
        numDigits = 0
        while numDigits + (9*(10**(i-1))*i) < n:
            numDigits += 9*(10**(i-1))*i
            i += 1
        val = 10**(i-1)
        val += (n-numDigits-1)//i
        numDigits += (n-numDigits-1)//i*i
        digit = (n-numDigits)
        return (val//(10**(i-digit)))%10

s = Solution()
print(s.findNthDigit(30))