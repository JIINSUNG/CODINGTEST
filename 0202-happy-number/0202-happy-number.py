class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        # 해피 넘버의 조건
        while True:
            cnt = 0
            for num in str(n):
                cnt += int(num) ** 2
            
            n = cnt
            
            if cnt == 1:
                return True
            
            if cnt in cycle:
                return False
            cycle.add(cnt)
            


        # 양의 정수로 시작하여 해당 숫자의 제곱의 합으로 숫자를 바꿉니다.
        # 숫자가 1이 될 때까지(그대로 유지됨) 프로세스를 반복하거나 1을 포함하지 않는 주기로 끝없이 반복됩니다.
        # 이 과정이 1로 끝나는 숫자는 행복합니다.