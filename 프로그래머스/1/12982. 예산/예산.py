def solution(d, budget):
    d.sort()  # 오름차순 정렬
    answer = 0
    
    for i in d:
        if budget >= i:
            budget -= i
            answer += 1
        else:
            break
    
    return answer