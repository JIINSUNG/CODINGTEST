from collections import defaultdict 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dictionary = defaultdict(list)
        candidates.sort()

        def dfs(index, current_sum, path):
            if current_sum == target:
                dictionary[target].append(path[:])
                return
            
            if current_sum > target:
                return
            
            for i in range(index, len(candidates)):
                dfs(i, current_sum + candidates[i], path + [candidates[i]])

        for candi in candidates:
            value = candi
            while value <= target:
                dictionary[value].append([candi] * (value//candi))
                value += candi

        dfs(0, 0, [])

        dictionary[target] = [list(t) for t in set(tuple(sorted(x)) for x in dictionary[target])]

        return dictionary[target]