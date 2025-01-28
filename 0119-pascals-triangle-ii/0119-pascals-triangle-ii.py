class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [[0] * i for i in range(1, rowIndex + 2) ]
        
        for i in range(rowIndex+1):
            answer[i][0] = 1
            answer[i][-1] = 1

        for i in range(2, rowIndex+1):
            for j in range(1, i):
                answer[i][j] = answer[i-1][j-1] + answer[i-1][j]

        return answer[rowIndex]        