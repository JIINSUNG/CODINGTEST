class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix[0])
        n = len(matrix)
        answer = 0

        def calculate(x, y, size):
            for i in range(x, x+size):
                for j in range(y, y+size):
                    if matrix[i][j] == 0:
                        return False
            return True



        for i in range(1, min(m, n)+1):
            for x in range(0, (n-i)+1):
                for y in range(0, (m-i)+1):
                    if calculate(x, y, i):
                        answer += 1
        return answer