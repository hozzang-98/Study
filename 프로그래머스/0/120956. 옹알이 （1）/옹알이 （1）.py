import re

def solution(babbling):
    
    pattern = re.compile(r'^(aya|ye|woo|ma)+$')
    answer = sum(1 for b in babbling if pattern.fullmatch(b))
    
    return answer