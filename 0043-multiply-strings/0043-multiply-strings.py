class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 둘 중 하나라도 0 이라면 곱했을때 결과는 0
        if num1 == '0' or num2 =='0':
            return '0'
        
        answer = 0
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                answer += int(num1[i]) * (10**(len(num1)-i-1)) * int(num2[j]) * (10**(len(num2)-j-1))
        return str(answer)

        

        

        
