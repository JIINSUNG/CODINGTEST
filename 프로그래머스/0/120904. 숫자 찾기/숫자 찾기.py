def solution(num, k):
    answer = 0
    
    return -1 if str(num).find(str(k)) == -1 else str(num).find(str(k)) +1