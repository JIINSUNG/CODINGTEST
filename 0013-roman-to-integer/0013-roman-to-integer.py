
class Solution:
    def romanToInt(self, s: str) -> int:
        # 7 개의 로만 심볼이 있음
        # 2 : II
        # 12 : X+II
        # 27 : XX+VII
        n = len(s)
        roman = {
            'I' : 1,
            'IV' : 4,
            'V' : 5,
            'X' : 10,
            'XL' : 40,
            'XC' : 90,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'CD' : 400,
            'CM' : 900,
            'M' : 1000
        }

        answer = 0
        i = 0
        while i < n: 
            if s[i] in ['I', 'X','C']:
                if s[i:i+2] in ['IV','XL','XC','CD','CM']:
                    answer += roman[s[i:i+2]]
                    i += 1
                else:
                    answer += roman[s[i]]
            else: 
                answer += roman[s[i]]
            i += 1
        return answer
        # C가 나오면 CD, CM인지 체크
        # X가 나오면 XL, XC인지 체크
        # I가 나오면 IV 인지 체크