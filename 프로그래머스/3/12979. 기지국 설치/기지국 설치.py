import math
def solution(n, stations, w):
    answer = 0
    position = 1
    
    for station in stations:
        target = station - w
        if position < target:
            gap = target - position
            answer += math.ceil(gap / (2*w+1))
        position = station + w + 1
    if position <= n:
        gap = n - position + 1
        answer += math.ceil(gap / (2*w+1))

    return answer