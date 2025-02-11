class Solution:
    def reverse(self, x: int) -> int:
        x = list(str(x))
        minus = False
        if x[0] == '-':
            minus = True
        
        if minus:
            value = x[:0:-1]
        else:
            value = x[::-1]
        answer = int(''.join(value))
        if minus:
            return -answer
        else:
            return answer

        
