class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        answer = []
        answer.append(pref[0]) 
        for i in range(1, n):
            answer.append(pref[i-1] ^ pref[i])
        return answer
