def solution(n):
    count = 0
    
    # k는 연속된 자연수의 개수 (1부터 n까지 시도)
    for k in range(1, n + 1):
        # n - k(k-1)/2가 k로 나누어떨어지는지 확인
        if (n - k * (k - 1) // 2) % k == 0 and (n - k * (k - 1) // 2) > 0:
            count += 1
    
    return count