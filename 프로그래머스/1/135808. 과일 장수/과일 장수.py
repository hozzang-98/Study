def solution(k, m, score):
    answer = 0

    score = sorted(score) # 1,1,1,2,2,3,3

    if len(score) < m:

        return 0
    
    while True:
        
        tmp = []
        
        for i in range(m):

            tmp.append(score.pop())

        answer += min(tmp) * len(tmp)

        if len(score) < m:

            break

    return answer