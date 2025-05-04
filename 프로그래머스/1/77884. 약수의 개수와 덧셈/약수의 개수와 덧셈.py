def solution(left, right):
    answer = 0
    
    for t in range(left, right+1):
        # 약수 개수가 홀수인 경우 → 제곱수인 경우!
        if int(t ** 0.5) ** 2 == t:
            answer -= t  # 홀수 개수면 빼기
        else:
            answer += t  # 짝수 개수면 더하기
            
    return answer