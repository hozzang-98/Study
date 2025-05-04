import re

def solution(files):
    def key_func(file):
        match = re.match(r'([^\d]+)(\d+)(.*)', file)  # HEAD, NUMBER, TAIL 추출
        head, number, tail = match.groups()
        return (head.lower(), int(number))  # 정렬 기준 적용

    return sorted(files, key=key_func)