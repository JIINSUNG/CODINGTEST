class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        flag = 0
        for i in range(1, n+1):
            flag += i

        return flag - sum(nums)    
