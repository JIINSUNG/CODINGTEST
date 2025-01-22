class Solution:
    def addBinary(self, a: str, b: str) -> str:
        cnt = int(a, 2) + int(b, 2)
        return bin(cnt)[2:]