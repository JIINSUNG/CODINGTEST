class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dx = [1, 1]
        dy = [-1, 1]
        n = len(mat)
        m = len(mat[0])
        answer = []

        graph = []
        for i in range(n):
            graph.append(mat[i] + [-100001])
        graph.append([-100001] * (m + 1))
        # 2 3 0
        # 0 0 0

        # 1 2 3 0
        # 4 5 6 0
        # 7 8 9 0
        # 0 0 0 0
        
        def traverse(x, y, is_right):
            if graph[x][y] != -100001:
                answer.append(graph[x][y])
            
            if x == n and y == m:
                return

            if is_right:
                nx = x - 1
                ny = y + 1
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    traverse(x, y+1, False) 
                else:
                    traverse(nx, ny, True)
            
            else:
                nx = x + 1
                ny = y - 1
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    traverse(x+1, y, True) 
                else:
                    traverse(nx, ny, False) 



        traverse(0, 0, True)

        return (answer)
