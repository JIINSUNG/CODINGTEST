class Solution:
    def toHex(self, num: int) -> str:
        # 32비트 정수로 처리
        if num == 0:
            return "0"
        
        # 음수일 경우 32비트 unsigned 정수로 변환
        if num < 0:
            num += 2**32
        
        # 16진수 변환
        hex_chars = "0123456789abcdef"
        result = ""
        
        while num > 0:
            result = hex_chars[num % 16] + result
            num //= 16
        
        return result