from collections import defaultdict 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dictionary = defaultdict(list)

        for candi in candidates:
            value = candi
            while value <= target:
                dictionary[value].append([candi] * (value//candi)) 
                value += candi
        
        for candi in candidates:
            value = candi
            while value <= target:
                if target - value < 0:
                    break

                for lists in dictionary[target-value]:
                    temp = sorted(lists + [candi] * (value//candi))
                    if temp not in dictionary[target]:
                        dictionary[target].append(temp) 
                value += candi
        return dictionary[target]