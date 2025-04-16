def solution(survey, choices):
    answer = ''
    dic = {'R':0, 'T':0, 'C':0, 'F':0,'J':0,'M':0, 'A':0, 'N':0}
    
    for sv, choice in zip(survey,choices):
        
        if choice > 4: # 동의 구간
            dic[sv[1]] += choice - 4
        else: # 비동의 구간
            dic[sv[0]] += 4 - choice

    if dic['R'] >= dic['T']: answer += 'R'
    else: answer += 'T'
        
    if dic['C'] >= dic['F']: answer += 'C'
    else: answer += 'F'
    
    if dic['J'] >= dic['M']: answer += 'J'
    else: answer += 'M'
    
    if dic['A'] >= dic['N']: answer += 'A'
    else: answer += 'N'
    
    return answer