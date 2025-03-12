from collections import defaultdict 
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            for j in range(i + 1, len(word) + 1):
                substring = word[i:j]
                char_count = defaultdict(int)
                
                for char in substring:
                    char_count[char] += 1
                
                # 홀수 번 출현하는 문자가 최대 하나인지 확인
                odd_count = sum(val % 2 for val in char_count.values())
                if odd_count <= 1:
                    count += 1
        
        return count
        
