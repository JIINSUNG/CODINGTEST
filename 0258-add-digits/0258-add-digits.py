class Solution:
    def addDigits(self, num: int) -> int:

        while len(str(num)) != 1:
            nums = list(str(num))
            num = 0
            for n in nums:
                num += int(n)
        return num    
