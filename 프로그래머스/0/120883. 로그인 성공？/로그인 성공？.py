def solution(id_pw, db):
    answer = ''
    
    dic = {i_p[0]: i_p[1] for i_p in db}
    
    if id_pw[0] in dic:
        if id_pw[1] == dic[id_pw[0]]:
            answer += 'login'
        elif id_pw[1] != dic[id_pw[0]]:
            answer += 'wrong pw'
    else:
        answer += 'fail'
            
    return answer