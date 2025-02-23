from collections import defaultdict 

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dictionary = defaultdict(list)
        candidates.sort()
        for candi in candidates:
            value = candi
            while value <= target:
                dictionary[value].append([candi] * (value//candi)) 
                value += candi
        
        for i in range(1, target+1):
            # i를 만든다고 생각하자
            for candi in candidates:
                if candi >= i or not candi:
                    break

                value = candi
                while value <= i:
                    if i - value < 0:
                        break

                    for lists in dictionary[i-value]:
                        temp = sorted(lists + [candi] * (value//candi))
                        if temp not in dictionary[i]:
                            dictionary[i].append(temp) 
                    value += candi
        return dictionary[target]