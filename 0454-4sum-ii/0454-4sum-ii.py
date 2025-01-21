from collections import defaultdict 
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        n = len(nums1)
        dictionary = defaultdict(int)

        for i in nums1:
            for j in nums2:
                dictionary[i+j] += 1
        
        cnt = 0

        for i in nums3:
            for j in nums4:
                cnt += dictionary[-i-j]
        return cnt
