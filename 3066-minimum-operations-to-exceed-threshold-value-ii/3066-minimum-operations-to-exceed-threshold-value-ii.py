import heapq
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        cnt = 0
        while True:
            if nums[0] >= k:
                return cnt
            cnt += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            heapq.heappush(nums, x*2 + y)
        
