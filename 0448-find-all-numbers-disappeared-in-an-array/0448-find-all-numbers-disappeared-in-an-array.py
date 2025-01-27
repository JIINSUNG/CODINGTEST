class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []

        
        def bisect_search(arr, target):
            left = 0
            right = len(arr)-1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False
        nums.sort()

        for i in range(1, len(nums)+1):
            if not bisect_search(nums, i):
                answer.append(i)
        return answer