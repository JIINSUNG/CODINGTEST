class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bisect_left(arr, target):
            left = 0
            right = len(arr)-1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1 
            return left
        
        return bisect_left(nums, target)