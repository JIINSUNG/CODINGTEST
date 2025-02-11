from itertools import combinations
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        subset = set()
        answer = []
        for i in range(n+1):
            for combi in combinations(nums, i):
                subset.add(combi)
        for combi in subset:
            sorted_list = sorted(combi)
            if not sorted_list in answer:
                answer.append(sorted_list)
        
        return answer