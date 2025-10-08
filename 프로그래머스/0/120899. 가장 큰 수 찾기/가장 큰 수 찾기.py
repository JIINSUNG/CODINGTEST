def solution(array):
    answer = [0, -1]
    
    for i in range(len(array)):
        if answer[0] < array[i]:
            answer[0] = array[i]
            answer[1] = i
    
    
    return answer