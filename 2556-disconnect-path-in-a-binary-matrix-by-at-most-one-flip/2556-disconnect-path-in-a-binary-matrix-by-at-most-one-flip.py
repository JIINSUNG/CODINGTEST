class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        
        def dfs(x, y):
            if x == n-1 and y == m-1:
                return True
            
            grid[x][y] = 0  
            
            for dx, dy in [(1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                    if dfs(nx, ny):
                        return True
            
            return False
        
        # 애초에 방문 할 수 없다면 
        if not dfs(0, 0):
            return True
        
        grid[0][0] = 1
        grid[n-1][m-1] = 1
        
        return not dfs(0, 0)

