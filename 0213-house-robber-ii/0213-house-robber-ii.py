class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_range(start: int, end: int) -> int:
            prev = curr = 0
            for i in range(start, end + 1):
                prev, curr = curr, max(curr, prev + nums[i])
            return curr

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        # 첫 번째 집을 포함하고 마지막 집을 제외한 경우와
        # 첫 번째 집을 제외하고 마지막 집을 포함한 경우 중 최대값 반환
        return max(rob_range(0, n-2), rob_range(1, n-1))

