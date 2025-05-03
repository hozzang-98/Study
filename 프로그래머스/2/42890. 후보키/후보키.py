from itertools import combinations

def solution(relation):
    answer = []
    
    n_cols = len(relation[0])
    n_rows = len(relation)
    
    # i개 짜리 조합 생성
    for i in range(1, n_cols+1):
        
        # 조합 인덱스 생성
        for combination in combinations(range(n_cols), i):
            
            tmp = [tuple([row[idx] for idx in combination]) for row in relation]
            
            if len(set(tmp)) < n_rows: continue
            
            flag = True
            
            for candidate in answer:
                
                if set(candidate).issubset(set(combination)):
                    
                    flag = False
                    break
                    
            if flag == True: answer.append(combination)
            
    
    return len(answer)