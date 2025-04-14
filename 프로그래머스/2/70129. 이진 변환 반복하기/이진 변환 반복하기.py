def solution(s):
    answer = [0,0]
    total_cnt = 0
    while s != '1':
        total_cnt += 1
        first = s.count('0')
        second = s.count('1')
        s = format(second,'b')
        answer[1] += first
    answer[0] += total_cnt
     
    return answer