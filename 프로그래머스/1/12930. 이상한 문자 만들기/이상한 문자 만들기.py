def solution(s):
    answer = ''
    s_list = s.split(' ')
    for li in s_list:
        for idx, c in enumerate(li):
            if idx % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '

    return answer[:-1]