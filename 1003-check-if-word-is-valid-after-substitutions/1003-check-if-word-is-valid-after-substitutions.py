class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 3: return False
    
        while s.find('abc') > -1:
            s = s.replace('abc','',1)
        
        return len(s) == 0