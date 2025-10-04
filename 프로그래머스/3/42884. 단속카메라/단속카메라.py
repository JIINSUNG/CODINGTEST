def solution(routes):
    answer = 0
    
    dist = -30001
    routes.sort(key= lambda x: x[1])
    
    for route in routes:
        if route[0] <= dist:
            continue
        else:
            answer += 1
            dist = route[1]
            
    return answer