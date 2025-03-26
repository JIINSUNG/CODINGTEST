class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        list2 = sum(grid, [])
        list2.sort()

        target = list2[len(list2)//2]
        answer = 0


        for value in list2:
            if abs(target-value) % x == 0:
               answer += abs(target-value) // x
            else:
                return -1
        return answer
    

