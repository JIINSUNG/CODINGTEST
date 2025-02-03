class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        candidate = -1


        for num in nums: 
            if count == 0:
                candidate = num
            
            if candidate == num:
                count += 1  
            else:
                count -= 1
        if nums.count(candidate) > len(nums) //2 :
            return candidate
        else:
            return -1