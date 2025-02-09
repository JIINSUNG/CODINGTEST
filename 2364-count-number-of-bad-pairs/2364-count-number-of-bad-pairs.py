class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j가 i보다 크고 
        # j - i != nums[j] - nums[i]이면 bad pair 이다
        # bad pair의 총 갯수를 출력하라
        cnt = 0 
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if j-i != nums[j] - nums[i]:
                    cnt += 1
        return cnt


