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
        row.sort()
        col.sort()
        previous = row[0]
        for i in range(1, len(row)):
            if row[i] == previous:
                connects[i-1] = True
                connects[i] = True
            previous = row[i]

        previous = col[0]
        for i in range(1, len(col)):
            if col[i] == previous:
                connects[i-1] = True
                connects[i] = True
            previous = col[i]
        print(connects)
        return connects.count(True)

