class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_pointer = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[unique_pointer - 1]:
                nums[unique_pointer] = nums[i]
                unique_pointer += 1

        return unique_pointer

