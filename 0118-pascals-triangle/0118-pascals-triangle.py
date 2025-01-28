class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[0] * i for i in range(1, numRows + 1) ]
        
        for i in range(numRows):
            answer[i][0] = 1
            answer[i][-1] = 1

        for i in range(2, numRows):
            for j in range(1, i):
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j]


        return answer