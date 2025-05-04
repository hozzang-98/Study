def solution(name, yearning, photo):
    
    answer = []
    
    dic = {n:score for n,score in zip(name,yearning)}

    for p in photo:

        tmp = 0

        for i in p:

            if i in dic.keys():
                tmp += dic[i]
            else:
                continue
            
        answer.append(tmp)
        
    
    return answer