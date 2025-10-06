import re 
def solution(my_string):
    answer = []

    return sorted(list(map(int, re.findall(r'\d', my_string))))