def solution(dot):
    
    if 0< dot[0] and 0 < dot[1]:
        return 1
    elif 0 < dot[0] and dot[1] < 0:
        return 4
    elif 0 > dot[0] and dot[1] > 0:
        return 2
    else:
        return 3