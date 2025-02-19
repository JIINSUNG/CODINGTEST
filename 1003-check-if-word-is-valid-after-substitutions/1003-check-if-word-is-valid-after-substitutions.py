class Solution:
    def isValid(self, s: str) -> bool:
        for i in range(len(s) // 3):
            s = s.replace('abc', '')
        
        if s:
            return False
        return True