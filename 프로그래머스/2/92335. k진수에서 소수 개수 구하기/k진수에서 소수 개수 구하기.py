def solution(n,k):
    
    answer = 0
    
    def n_to_k(n,k): # 숫자 n을 k진법으로 변환
        k_num = ''
        while n >= 1:
            n,mod = divmod(n,k) # (몫, 나머지 )
            k_num += str(mod) # 나머지를 string에 추가
            change = k_num[::-1].split('0') # 역순으로 해 0을 기준으로 split
        return change

    def prime_number(k): # 소수 판별 
        if k == 1:
            return False
        elif k == 2 or k == 3:
            return True
        for j in range(3,int(k**0.5+1),2): # 빠르게 소수를 판별하려면 자기 자신의 루트 값까지만 확인하면 됨
                if k % j == 0:
                    return False
        return True

    ntk = n_to_k(n,k)

    for i in ntk:

        if i == '':

            continue

        elif prime_number(int(i))==True:
            answer += 1
    
    return answer