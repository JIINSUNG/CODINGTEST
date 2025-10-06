import re
def solution(my_string):
    answer = 0
    
    for num in re.findall(r'[0-9]', my_string):
        answer += int(num)
        
    return answer