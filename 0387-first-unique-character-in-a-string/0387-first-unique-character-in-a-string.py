
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)

        for key, value in counter.items():
            if value == 1:
                return s.index(key)
        return -1
        

