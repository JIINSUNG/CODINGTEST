class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zeroCnt = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroCnt += 1
        
        for i in range(zeroCnt):
            nums.remove(0)
        
        for i in range(zeroCnt):
            nums.append(0)
        