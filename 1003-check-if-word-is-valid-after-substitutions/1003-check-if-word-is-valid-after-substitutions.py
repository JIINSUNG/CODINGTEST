class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s) // 3):
            s = s.split('abc')
            s = ''.join(s)
        
        if s:
            return False
        return True
