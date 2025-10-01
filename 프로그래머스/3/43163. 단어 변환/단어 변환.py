from collections import deque
import math
def solution(begin, target, words):
    
    answer = float('inf')
    
    
    def isCanChange(word1, word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt +=1
                
            if cnt >= 2:
                break
        return cnt == 1
    
    
    def bfs(depth, start):
        queue = deque()
        visited = set()    
        queue.append([depth, start])
        
        while queue:
            d, cword = queue.popleft()
            if cword == target:
                return d 
                
            for word in words:
                if not (word in visited) and isCanChange(cword, word):
                    queue.append([d+1, word])
                    visited.add(word)
                    
        return 0
                    
                
            
        
        
        
    return bfs(0, begin)
    