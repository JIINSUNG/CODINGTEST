class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(arr):
            max_sum = arr[0]
            curr_sum = arr[0]
            for num in arr[1:]:
                curr_sum = max(num, curr_sum + num)
                max_sum = max(max_sum, curr_sum)
            return max_sum
        
        total_sum = sum(nums)
        max_sum = kadane(nums)
        
        # 모든 요소가 음수인 경우
        if max_sum <= 0:
            return max_sum
        
        min_sum = -kadane([-num for num in nums])
        return max(max_sum, total_sum - min_sum)