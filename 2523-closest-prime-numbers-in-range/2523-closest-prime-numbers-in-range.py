class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # left <= num1 < num2 <= right 을 만족하는 
        # 소수 num1, num2를 찾돼, 그 갭이 최소가 되는 num1, num2 구하기
        # 만약 없다면 [-1, -1] 리턴


        answer = [-1, -1]
        primes = [True] * (right+1)
        primes[0] = False
        primes[1] = False

        candidate = []
        dist = float('inf')


        for i in range(2, int(right**0.5)+1):
            if primes[i]:
                for j in range(i*2, right+1, i):
                    primes[j] = False
        before = -1

        for i in range(left, right+1):
            # i가 소수 일때
            if primes[i]:
                if before == -1:
                    before = i

                else:
                    if (i - before) < dist:
                        dist = i - before
                        answer[0] = before
                        answer[1] = i
                    before = i


        return answer


            