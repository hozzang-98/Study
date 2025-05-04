def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1,int(total**0.5)+1): # 1~7
        if total % i == 0:
            a = i # 1, 2 ,3 , 4, 6, 
            b = total // i # 48, 24, 16, 12, 8
            if 2*(a+b-2) == brown:
                answer.append(b)
                answer.append(a)

    return answer