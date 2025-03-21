class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        dictionary = defaultdict(int)
        for i in range(len(nums)):
            nums[i] = i - nums[i]
            dictionary[nums[i]] += 1

        total = len(nums)
        cnt = 0
        for i in range(len(nums)):
            dictionary[nums[i]]-= 1
            total -= 1
            cnt += total - dictionary[nums[i]]
        return cnt


