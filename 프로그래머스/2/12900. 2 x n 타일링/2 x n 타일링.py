def solution(n):
    if n == 1:
        return 1  # n=1일 때는 경우의 수 1
    
    a, b = 1, 2  # n=1일 때(1개), n=2일 때(2개) 초기값 설정
    for _ in range(2, n):
        a, b = b, (a + b) % 1000000007  # 이전 두 개의 값을 업데이트
        
    return b  # n번째 값 반환