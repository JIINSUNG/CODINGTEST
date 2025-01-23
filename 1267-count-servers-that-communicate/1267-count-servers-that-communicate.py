class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row = []
        col = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    row.append(i)
                    col.append(j)

        connects = [False] * len(row)

        for i in range(len(row)):
            for j in range(i+1, len(row)):
                if row[i] == row[j]:
                    connects[i] = True
                    connects[j] = True

        previous = col[0]
        for i in range(len(col)):
            for j in range(i+1, len(col)):
                if col[i] == col[j]:
                    connects[i] = True
                    connects[j] = True
        return connects.count(True)

