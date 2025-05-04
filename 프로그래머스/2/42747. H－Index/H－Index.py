def solution(citations):
    
    citations.sort() # 0,1,3,5,6
    n = len(citations)
    answer = 0

    for i in range(n): # 0~4
        h = n - i # 5,4,3,2,1

        if citations[i] >= h:
            answer = h
            break

    return answer