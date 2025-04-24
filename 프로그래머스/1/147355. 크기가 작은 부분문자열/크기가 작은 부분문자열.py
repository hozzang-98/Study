def solution(t, p):
    
    answer = 0
    tmp_list = []
    
    idx = 0
    for i in range(len(t)-len(p)+1):
        
        tmp_list.append(int(''.join(t[i:i+len(p)])))

    return len([i for tmp in tmp_list if tmp <= int(p)]) 