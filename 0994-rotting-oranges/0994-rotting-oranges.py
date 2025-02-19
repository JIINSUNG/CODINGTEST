class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        answer = 0
        while queue and fresh != 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
            answer += 1
        if fresh == 0:
            return answer
        else:
            return -1

