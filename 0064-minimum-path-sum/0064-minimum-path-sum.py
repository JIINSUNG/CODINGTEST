class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        self.answer = [[float('inf')] * m for _ in range(n)]
        
        self.answer[0][0] = grid[0][0]
        dx = [0, 1]
        dy = [1, 0]

        def bfs(i, j):
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()

                for k in range(2):
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if 0 <= nx < n and 0 <= ny < m and self.answer[nx][ny] > self.answer[x][y] + grid[nx][ny]:
                        self.answer[nx][ny] = self.answer[x][y] + grid[nx][ny]
                        queue.appendleft((nx, ny))
        
        bfs(0, 0)

        print(self.answer)
        return self.answer[n-1][m-1]



                    


        


  