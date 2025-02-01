class Solution:
    def jump(self, nums: List[int]) -> int:
        # 길이가 n이고 인덱스가 0인 정수 배열이 제공됩니다. 처음에는 nums[0]에 위치합니다.
        # 각 요소 nums[i]는 인덱스 i에서 앞으로 점프하는 최대 길이를 나타냅니다. 즉, nums[i]에 있는 경우 임의의 nums[i + j]로 이동할 수 있습니다.
        # 0 <= j <= nums[i]
        # i+j < n
        # 최소 점프 수를 반환하라 nums[n-1] 에 도달하는
        n = len(nums)
        dp = [i for i in range(n)]
        
        for i in range(n):
            pos = dp[i] + nums[i]
            if pos < n:
                dp[pos] = min(dp[pos], dp[i]+1)
        
        return dp[n-1]
            



