class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        row = [0] * n
        col = [0] * m


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
        
        answer = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (row[i] >= 2 or col[j] >= 2):
                    answer += 1
        return answer

        
