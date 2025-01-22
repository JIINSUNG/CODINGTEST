class Solution:
    def mySqrt(self, x: int) -> int:
        cnt = 1

        while True:
            if cnt * cnt > x:
                cnt -= 1
                break
            elif cnt * cnt == x:
                break 
            cnt += 1
        return cnt