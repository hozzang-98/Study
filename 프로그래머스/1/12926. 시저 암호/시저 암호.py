def solution(s, n):
    
    answer = ''
    
    upper_dic = {chr(65+i):i for i in range(26)}
    upper_reverse = {v:k for k,v in upper_dic.items()}
    
    lower_dic = {chr(97+i):i for i in range(26)}
    lower_reverse = {v:k for k,v in lower_dic.items()}
    
    for _ in s:
        if _.isupper():
            answer += upper_reverse[(upper_dic[_] + n)%26]
        elif _.islower():
            answer += lower_reverse[(lower_dic[_] + n)%26]
        else:
            answer += ' '
            
    return answer