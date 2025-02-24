import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        # 분수 덧셈과 뺄셈의 표현을 나타내는 문자열 표현식이 주어졌을 때, 계산 결과를 문자열 형식으로 반환합니다.
        # 최종 결과는 기약 분수여야 합니다. 최종 결과가 정수인 경우 분모가 1인 분수 형식으로 변경합니다. 따라서 이 경우 2는 2/1로 변환해야 합니다.
        분자 = []
        분모 = []
        
        isMinus = False
        분자차례 = True
        digit = ''
        
        for i in range(len(expression)):
            if expression[i] in ['-', '+']: # 기호가 나오고, 부모 차례라면
                if not 분자차례:
                    분모.append(int(digit))
                    digit = ''
                    분자차례 = True

                if expression[i] == '-':
                    isMinus = True

            # 숫자야?
            elif expression[i].isdigit():
                digit += expression[i]
                
            
            elif expression[i] == '/':
                if isMinus:
                    분자.append(-int(digit))
                    isMinus = False
                else:
                    분자.append(int(digit))
                digit = ''
                분자차례 = False
        if digit:
            분모.append(int(digit))
                
        분모copy = set(분모)
        lcm = 1
        for 인자 in 분모copy:
            lcm *= 인자         
        
        for i in range(len(분자)):
            분자[i] *= lcm // 분모[i]
        
        result = sum(분자)
        if result == 0:
            return(f"{result}/1")
        else:
            gcd = math.gcd(result, lcm)
            return(f"{result//gcd}/{lcm//gcd}")

        # 분자, 분모를 통일 시키기


