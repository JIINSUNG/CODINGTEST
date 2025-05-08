class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for r in range(m + 1)]
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    dp[r][c] = min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1]) + 1
        ans = 0
        for r in range(m):
            ans += sum(dp[r])
        return ans



        for i in range(1, min(m, n)+1):
            for x in range(0, (n-i)+1):
                for y in range(0, (m-i)+1):
                    if calculate(x, y, i):
                        answer += 1
        return answer