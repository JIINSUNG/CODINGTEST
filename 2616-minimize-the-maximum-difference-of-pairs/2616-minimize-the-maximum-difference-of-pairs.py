class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        left = 0 
        right = nums[-1] - nums[0]


        def can_make(target):
            pairs = 0
            i = 0 
            while i < len(nums)-1:
                if nums[i+1] - nums[i] <= target:
                    pairs += 1
                    i += 2
                else:
                    i += 1
            if pairs >= p:
                return True
            return False

                

        while left <= right:
            mid = (left + right) // 2
            if can_make(mid):
                right = mid -1 
            else:
                left = mid + 1 
        
        return left
