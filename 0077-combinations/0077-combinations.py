class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]

        answer = []
        for combi in combinations(nums, k):
            answer.append(list(combi))
        return answer